# WP-034: Day 4 Reconciliation and Legacy-Framing Sweep

**Status:** Active — pending Principal Investigator review  
**Parents:** WP-028, WP-029, WP-033  
**Origin:** thinx-gpt post-tune-up recommendations (ai-bridge, 2026-10-06), steps 1 and 2 of the agreed execution order

## Objective

1. Reconcile the recovered foundations paper (WP-033) with the asynchronous Day 4 architecture so it no longer implies an older cosmology in which genuine external history and propagation are merely a residual problem.
2. Verify that no other document silently conflicts with the current both-and initialization / asynchronous-deployment architecture.

## 1. Foundations paper reconciliation

Revised in [`drafts/foundations-actualization-agency-intelligibility.md`](../drafts/foundations-actualization-agency-intelligibility.md): abstract, §8.5 (retitled "The residual, relocated"), §8.6, and the conclusion. A revision note at the head of the paper points to the preserved original (tag `archive/wp-002-foundations-paper`).

Substance of the change:

- Under WP-028/WP-029 the external cosmos genuinely executes its history, so supernova light curves and eclipsing-binary records are real traces of real events. The fabrication residual (Class C applied to the heavens) is empty by construction.
- The burden relocates rather than vanishes: roughly 13.8 Gyr of external process time against about one terrestrial day (ratio near 5.04 × 10^12) must be synchronized without contradiction. The paper now states that the screened candidate realizations have not derived the ratio economically, citing WP-029/WP-030 as recorded.
- §8.6 gains a discriminator: if no synchronization mechanism can be specified that forbids some observation, the architecture is an empirically idle auxiliary and is recorded as a debit. This links the paper to the D3 question.
- Sections 1 to 7 are untouched. The companion-paper framing remains a separate WP-033 item.

## 2. Legacy-framing sweep

Method (reproducible):

```text
git grep -n -i -E "light in transit|light-in-transit|in transit|created light|light created|appearance of age|appearance-of-age|mature creation|starlight problem|distant starlight|light-travel|light travel time|white.?hole|anisotropic synchron|Lisle|Humphreys|c-decay|light.?speed decay|prochron" -- '*.md'
```

Every hit was reviewed. Results:

| File | Hits | Disposition |
|---|---:|---|
| `drafts/foundations-actualization-agency-intelligibility.md` | 10 | Revised (section 1 above) |
| `work-packages/WP-032-historical-integrity-macro-state-initialization.md` | 19 | Conflict, **resolved**: allocation deferred to Day 4 (below) |
| `work-packages/WP-003-supernova-functional-state-hypothesis.md` | 3 | **Conflict, already scheduled**: WP-028's propagation table lists "WP-003 supernova: convert initialization-vs-history framing to mixed allocation", not yet done. Reconciliation note added at the head of WP-003; full conversion remains open. |
| `drafts/designed-functional-maturity.md` | 4 | Consistent. Line ~400 already states WP-028 replaces "starlight in transit" with mixed allocation; the appearance-of-age passages are generic. |
| `work-packages/WP-028-…`, `WP-028/day4-layered-hypothesis-registry.md` | 4 | Consistent (they disclaim white-hole / anisotropic-synchrony mechanisms). |
| `work-packages/WP-033-foundations-paper-recovery.md` | 2 | Updated: open item 2 marked done by this WP. |
| `PROGRAMME.md` | 1 | Consistent (generic coherence principle). |

### Decision required: WP-032 supernova category (3)

WP-032 §"Supernova application" allows a named supernova to be classified as "(3) part of a coherently pre-seeded cosmic event-state or causal structure integrated into the initialized heavens."

For phenomena in the external cosmos this conflicts with the frozen Day 4 boundary: WP-029 places genuine stellar evolution and supernovae in the deployment payload, and WP-030 was closed precisely because reallocating observed external states to initialization "changed the hypothesis rather than testing it." Left as written, category (3) reopens the WP-030 move for supernovae.

**Resolved 2026-10-06 (JD: "move to Day 4").** External-cosmos allocation is deferred to the Day 4 architecture; a "Day 4 deferral" paragraph was added to WP-032 §"Supernova application" in this WP. The originally proposed wording was:

> Under the frozen asynchronous Day 4 hypothesis (WP-029), category (3) is not available for external-cosmos supernovae: their events belong to the genuinely executed deployment payload. Category (3) remains a terrestrial- or boundary-domain category and may be applied to external phenomena only through a recorded revision of the WP-029 boundary, not case by case.

Alternative: keep category (3) and record an explicit amendment to the WP-029 boundary explaining when external event-states may be initialized. Either way the choice should be explicit, not left to case-by-case allocation.

## Next

D3 candidate generation opens as its own work package after this WP is reviewed, with preregistration of candidate consequences and failure conditions, and with a null result ("no discriminating consequence") recorded as a debit.

Human-Curated, AI-Enabled (HCAE)
