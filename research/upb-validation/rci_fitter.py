"""Shared-parameter multi-grain RCI fitter (synthetic validation stage).

Implements the RCI model of DFM_UPb_Validation_Protocol_v0.1 exactly in
the form the protocol states it, for ideal closed-system post-closure
evolution: with a206 = D206*(0)/P238(0) and a207 = D207*(0)/P235(0),

    D206*(t)/P238(t) = (a206 + 1) exp(lambda238 t) - 1
    D207*(t)/P235(t) = (a207 + 1) exp(lambda235 t) - 1

which is upb_baseline.initialized(). The initial ratios are SHARED
parameters: one (a206, a207) pair per fitted group, never one per grain
or per sample (gate item 6; a freely tuned initial daughter ratio per
sample is a declared failure mode of the protocol). Each fitted unit
(sample) carries its own closure age; the initialization parameters are
shared across all grains of the unit, or across all units of a group in
fit_group(). Earth initialization time and individual closure times are
not conflated: the shared initials describe the inventory at each
unit's closure under the model, which is the only reading the current
documents support (see the underspecification notes in the PR body).

Likelihoods use only the published per-analysis Error_Correlation via
upb_covariance.py. No covariance is inferred or fabricated. Common Pb,
disequilibrium, Pb loss and shared systematic uncertainties are not
modeled (gate: current implementation boundary).

IDENTIFIABILITY (a structural property of the model as specified,
verified by the synthetic tests): the initialized curve obeys the
exact identity initialized(t + dt, a') = initialized(t, a) with
a' = (a + 1) exp(-lambda dt) - 1 applied per ratio. So with the initial
ratios free and every unit's age free, the likelihood is exactly
invariant under a uniform translation of all ages. Age and shared
initials are then NOT separately identifiable, at unit level or group
level. This is the protocol's own warning ("time and initial inventory
are not identifiable" when initials are free) in exact form. The
protocol and gate resolve it by requiring the RCI parameters to be
constrained independently of the fitted ratios. Accordingly:
- fit_unit / fit_group without constraints return chi-square and
  log-likelihood (which are invariant and well defined) plus a
  deterministic REPRESENTATIVE of the equivalence family: the optimum
  is translated exactly along the family (ages up, initials down by
  the identity above) until the first initial ratio reaches zero,
  which is the minimum-initial-inventory member of the family. That
  convention is a deterministic reporting rule, not identification,
  and results say so. Reported chi-square and log-likelihood are
  recomputed at the canonical representative.
- fit_group accepts anchor_ages (independently known ages for named
  units) and fixed_initials (independently constrained initials);
  either breaks the translation invariance and makes the remaining
  parameters identifiable. Supplying such constraints from independent
  evidence is a predeclare decision, not made here.

GAPS in the current documents, not resolved by invention here:
- No numeric bounds for a206/a207 are declared anywhere yet; the gate
  requires initialization parameter bounds to be frozen before fitting
  real data. The defaults below are caller-adjustable placeholders for
  synthetic work only, NOT frozen program values.
- The grouping granularity for sharing (unit vs geological/mineralogical
  group) is named by the gate but no concrete grouping is predeclared;
  both levels are exposed (fit_unit, fit_group) for the predeclare step.
- No independent constraint set (anchors or fixed initials) is declared
  in the documents yet; without one, only fit statistics, not ages or
  initials, are identifiable outputs of this model.

The optimizer is a deterministic Nelder-Mead search implemented here
with fixed starting points and fixed simplex steps: same inputs always
produce the same outputs.
"""
import math
from upb_baseline import initialized
from upb_covariance import RatioObservation, mahalanobis2, log_likelihood

# Placeholder synthetic-work bounds for the shared initial ratios.
# NOT frozen program values; see module docstring.
DEFAULT_INITIAL_UPPER = 10.0


def _nelder_mead(objective, start, steps, *, max_iter=3000, tol=1e-9):
    """Deterministic Nelder-Mead simplex minimization (stdlib only)."""
    n = len(start)
    simplex = [list(start)]
    for i in range(n):
        point = list(start)
        point[i] += steps[i]
        simplex.append(point)
    values = [objective(p) for p in simplex]
    for _ in range(max_iter):
        order = sorted(range(n + 1), key=lambda i: values[i])
        simplex = [simplex[i] for i in order]
        values = [values[i] for i in order]
        spread = max(abs(values[i] - values[0]) for i in range(1, n + 1))
        size = max(abs(simplex[i][j] - simplex[0][j])
                   for i in range(1, n + 1) for j in range(n))
        if spread < tol and size < tol:
            break
        centroid = [sum(simplex[i][j] for i in range(n)) / n for j in range(n)]
        worst = simplex[n]
        reflected = [centroid[j] + (centroid[j] - worst[j]) for j in range(n)]
        f_reflected = objective(reflected)
        if f_reflected < values[0]:
            expanded = [centroid[j] + 2.0 * (centroid[j] - worst[j]) for j in range(n)]
            f_expanded = objective(expanded)
            if f_expanded < f_reflected:
                simplex[n], values[n] = expanded, f_expanded
            else:
                simplex[n], values[n] = reflected, f_reflected
        elif f_reflected < values[n - 1]:
            simplex[n], values[n] = reflected, f_reflected
        else:
            if f_reflected < values[n]:
                contracted = [centroid[j] + 0.5 * (reflected[j] - centroid[j])
                              for j in range(n)]
                f_contracted = objective(contracted)
                if f_contracted <= f_reflected:
                    simplex[n], values[n] = contracted, f_contracted
                    continue
            else:
                contracted = [centroid[j] - 0.5 * (centroid[j] - worst[j])
                              for j in range(n)]
                f_contracted = objective(contracted)
                if f_contracted < values[n]:
                    simplex[n], values[n] = contracted, f_contracted
                    continue
            best = simplex[0]
            for i in range(1, n + 1):
                simplex[i] = [best[j] + 0.5 * (simplex[i][j] - best[j])
                              for j in range(n)]
                values[i] = objective(simplex[i])
    order = sorted(range(n + 1), key=lambda i: values[i])
    return simplex[order[0]], values[order[0]]


def _bounded(objective, bounds):
    """Wrap an objective with a quadratic penalty outside the bounds."""
    def wrapped(x):
        penalty = 0.0
        for value, (lo, hi) in zip(x, bounds):
            if value < lo:
                penalty += (lo - value) ** 2
            elif value > hi:
                penalty += (value - hi) ** 2
        if penalty:
            return 1e12 + 1e12 * penalty
        return objective(x)
    return wrapped


def _validate_observations(observations):
    observations = list(observations)
    if not observations:
        raise ValueError('empty unit: at least one analysis is required')
    for o in observations:
        if not isinstance(o, RatioObservation):
            raise TypeError('observations must be RatioObservation instances')
        o.validate()
    return observations


def _best_age_zero_initial(observations, max_age_years):
    """Coarse deterministic age bracket at zero initial inventory."""
    def score(t):
        return sum(mahalanobis2(o, initialized(t, 0.0, 0.0)) for o in observations)
    n = 256
    step = max_age_years / n
    j = min(range(n + 1), key=lambda i: score(i * step))
    return j * step, score(j * step)


def _unit_chi2(observations, age_years, initial68, initial75):
    prediction = initialized(age_years, initial68, initial75)
    return sum(mahalanobis2(o, prediction) for o in observations)


def _unit_log_likelihood(observations, age_years, initial68, initial75):
    prediction = initialized(age_years, initial68, initial75)
    return sum(log_likelihood(o, prediction) for o in observations)


def unit_parameter_count(n_analyses, *, initials_free=True):
    """One closure age plus the two shared initial ratios, for any n.
    With independently fixed initials only the age is free."""
    if n_analyses < 1:
        raise ValueError('empty unit')
    return 3 if initials_free else 1


def fit_unit(observations, *, max_age_years=4.6e9,
             initial_bounds=(0.0, DEFAULT_INITIAL_UPPER),
             fixed_initials=None):
    """Fit one unit: shared (a206, a207) across all its grains, one age.

    Deterministic multi-start Nelder-Mead over (age, a206, a207), or
    over the age alone when fixed_initials supplies independently
    constrained initials. Without fixed initials the result carries
    the unanchored identifiability flag described in the module
    docstring; chi-square and log-likelihood are unaffected by that
    degeneracy, the returned age/initials are a representative.
    """
    observations = _validate_observations(observations)
    lo, hi = initial_bounds
    if not (math.isfinite(max_age_years) and max_age_years > 0):
        raise ValueError('invalid model bounds')
    if not (0.0 <= lo < hi and math.isfinite(hi)):
        raise ValueError('invalid initial-ratio bounds')
    if fixed_initials is not None:
        f68, f75 = fixed_initials
        if not (lo <= f68 <= hi and lo <= f75 <= hi):
            raise ValueError('fixed initials outside initial bounds')

        def objective(x):
            return _unit_chi2(observations, x[0], f68, f75)

        bounded = _bounded(objective, [(0.0, max_age_years)])
        t0, _ = _best_age_zero_initial(observations, max_age_years)
        x, _f = _nelder_mead(bounded, [t0], [max(0.02 * t0, 1e6)])
        age, a68, a75 = x[0], f68, f75
        k = unit_parameter_count(len(observations), initials_free=False)
        identifiability = 'initials_fixed_independently'
    else:
        t0, _ = _best_age_zero_initial(observations, max_age_years)
        bounds = [(0.0, max_age_years), (lo, hi), (lo, hi)]

        def objective(x):
            return _unit_chi2(observations, x[0], x[1], x[2])

        bounded = _bounded(objective, bounds)
        age_step = max(0.02 * t0, 1e6)
        starts = [
            (t0, 0.0, 0.0),
            (t0, 0.1, 0.1),
            (t0, 0.05, 0.3),
            (min(t0 * 1.05, max_age_years), 0.3, 0.05),
        ]
        best_x, best_f = None, None
        for start in starts:
            start = [min(max(start[i], bounds[i][0]), bounds[i][1])
                     for i in range(3)]
            x, f = _nelder_mead(bounded, start, [age_step, 0.05, 0.05])
            if best_f is None or f < best_f:
                best_x, best_f = x, f
        ages_c, a68, a75 = _canonicalize([best_x[0]], best_x[1],
                                         best_x[2], max_age_years)
        age = ages_c[0]
        k = unit_parameter_count(len(observations))
        identifiability = 'unanchored_translation_degenerate'
    return {
        'age_years': age,
        'initial68': a68,
        'initial75': a75,
        'chi2': _unit_chi2(observations, age, a68, a75),
        'log_likelihood': _unit_log_likelihood(observations, age, a68, a75),
        'n_analyses': len(observations),
        'parameter_count': k,
        'degrees_of_freedom': 2 * len(observations) - k,
        'initial_bounds': (lo, hi),
        'identifiability': identifiability,
    }


def group_parameter_count(n_units, n_analyses_total, *,
                          n_anchored_ages=0, initials_free=True):
    """Shared (a206, a207) if free, plus one closure age per unanchored
    unit, for any grain count."""
    if n_units < 1 or n_analyses_total < n_units:
        raise ValueError('invalid group shape')
    if not 0 <= n_anchored_ages <= n_units:
        raise ValueError('invalid anchor count')
    return (2 if initials_free else 0) + (n_units - n_anchored_ages)


def fit_group(units, *, max_age_years=4.6e9,
              initial_bounds=(0.0, DEFAULT_INITIAL_UPPER),
              anchor_ages=None, fixed_initials=None):
    """Fit a predeclared group of units with ONE shared (a206, a207).

    units: mapping of unit id -> list of RatioObservation. Each unit
    keeps its own closure age; the initial ratios are shared across
    every grain of every unit in the group. This is the gate item 6
    sharing structure.

    anchor_ages: optional mapping of unit id -> independently known
    age in years; anchored ages are held fixed, not fitted.
    fixed_initials: optional (a206, a207) pair constrained
    independently of the fitted ratios; held fixed, not fitted.
    Either constraint breaks the translation degeneracy described in
    the module docstring; with neither, the result is flagged
    unanchored and only the fit statistics are identifiable outputs.
    Deterministic multi-start Nelder-Mead over the free parameters.
    """
    if not units:
        raise ValueError('empty group')
    unit_ids = sorted(units)
    cleaned = {uid: _validate_observations(units[uid]) for uid in unit_ids}
    lo, hi = initial_bounds
    if not (math.isfinite(max_age_years) and max_age_years > 0):
        raise ValueError('invalid model bounds')
    if not (0.0 <= lo < hi and math.isfinite(hi)):
        raise ValueError('invalid initial-ratio bounds')
    anchor_ages = dict(anchor_ages or {})
    for uid, age in anchor_ages.items():
        if uid not in cleaned:
            raise ValueError('anchor age for unknown unit: ' + str(uid))
        if not (math.isfinite(age) and 0.0 <= age <= max_age_years):
            raise ValueError('anchor age out of bounds')
    if fixed_initials is not None:
        f68, f75 = fixed_initials
        if not (lo <= f68 <= hi and lo <= f75 <= hi):
            raise ValueError('fixed initials outside initial bounds')
    free_units = [uid for uid in unit_ids if uid not in anchor_ages]
    ages0 = {uid: _best_age_zero_initial(cleaned[uid], max_age_years)[0]
             for uid in free_units}

    # Free-parameter vector layout: [a68, a75] (unless fixed), then one
    # age per free unit, in sorted unit order.
    def unpack(x):
        if fixed_initials is not None:
            a68, a75 = fixed_initials
            rest = x
        else:
            a68, a75 = x[0], x[1]
            rest = x[2:]
        ages = {}
        for i, uid in enumerate(free_units):
            ages[uid] = rest[i]
        for uid, age in anchor_ages.items():
            ages[uid] = age
        return a68, a75, ages

    def objective(x):
        a68, a75, ages = unpack(x)
        return sum(_unit_chi2(cleaned[uid], ages[uid], a68, a75)
                   for uid in unit_ids)

    bounds = []
    if fixed_initials is None:
        bounds += [(lo, hi), (lo, hi)]
    bounds += [(0.0, max_age_years)] * len(free_units)

    def start_vector(a68, a75, scale):
        head = [] if fixed_initials is not None else [a68, a75]
        return head + [min(ages0[uid] * scale, max_age_years)
                       for uid in free_units]

    starts = [start_vector(0.0, 0.0, 1.0),
              start_vector(0.1, 0.1, 1.0),
              start_vector(0.05, 0.3, 1.05)]
    steps = [] if fixed_initials is not None else [0.05, 0.05]
    steps += [max(0.02 * ages0[uid], 1e6) for uid in free_units]
    bounded = _bounded(objective, bounds)
    best_x, best_f = None, None
    for start in starts:
        start = [min(max(start[i], bounds[i][0]), bounds[i][1])
                 for i in range(len(start))]
        x, f = _nelder_mead(bounded, start, steps)
        if best_f is None or f < best_f:
            best_x, best_f = x, f
    a68, a75, ages = unpack(best_x)
    if fixed_initials is None and not anchor_ages:
        age_list, a68, a75 = _canonicalize(
            [ages[uid] for uid in unit_ids], a68, a75, max_age_years)
        ages = {uid: age_list[i] for i, uid in enumerate(unit_ids)}
    total_n = sum(len(cleaned[uid]) for uid in unit_ids)
    k = group_parameter_count(len(unit_ids), total_n,
                              n_anchored_ages=len(anchor_ages),
                              initials_free=fixed_initials is None)
    per_unit = {}
    total_ll = 0.0
    for uid in unit_ids:
        ll = _unit_log_likelihood(cleaned[uid], ages[uid], a68, a75)
        total_ll += ll
        per_unit[uid] = {
            'age_years': ages[uid],
            'chi2': _unit_chi2(cleaned[uid], ages[uid], a68, a75),
            'log_likelihood': ll,
            'n_analyses': len(cleaned[uid]),
            'anchored': uid in anchor_ages,
        }
    if fixed_initials is not None:
        identifiability = 'initials_fixed_independently'
    elif anchor_ages:
        identifiability = 'anchored_by_independent_age'
    else:
        identifiability = 'unanchored_translation_degenerate'
    return {
        'initial68': a68,
        'initial75': a75,
        'units': per_unit,
        'chi2': sum(_unit_chi2(cleaned[uid], ages[uid], a68, a75)
                    for uid in unit_ids),
        'log_likelihood': total_ll,
        'n_units': len(unit_ids),
        'n_analyses': total_n,
        'parameter_count': k,
        'degrees_of_freedom': 2 * total_n - k,
        'initial_bounds': (lo, hi),
        'identifiability': identifiability,
    }


def translated_initials(age_shift_years, initial68, initial75):
    """The exact translation family of the module docstring: shifting
    every age by dt and mapping the initials per ratio leaves every
    prediction unchanged. Exposed so tests and the predeclare step can
    reason about the degeneracy explicitly."""
    from upb_baseline import L238, L235
    import math as _math
    return ((initial68 + 1) * _math.exp(-L238 * age_shift_years) - 1,
            (initial75 + 1) * _math.exp(-L235 * age_shift_years) - 1)


def _canonicalize(ages, initial68, initial75, max_age_years):
    """Translate an unanchored optimum along its exact equivalence
    family to the minimum-initial-inventory member: shift all ages up
    by the largest dt that keeps every age within bounds and drives
    the first initial ratio exactly to zero (both ratios decrease
    monotonically under the translation, so the first zero crossing
    minimizes |a206| + |a207| over the feasible family)."""
    from upb_baseline import L238, L235
    dt = max_age_years - max(ages)
    for a, lam in ((initial68, L238), (initial75, L235)):
        if a > 0:
            dt = min(dt, math.log1p(a) / lam)
    if dt <= 0:
        return list(ages), initial68, initial75
    a68, a75 = translated_initials(dt, initial68, initial75)
    return [t + dt for t in ages], max(a68, 0.0), max(a75, 0.0)
