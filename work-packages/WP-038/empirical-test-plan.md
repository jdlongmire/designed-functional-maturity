# WP-038 Empirical Test Plan

## Dataset requirements
Preselect orthologous human/chimp ERV loci and appropriate gorilla/orangutan/outgroup loci; record build, assembly confidence, coordinates, flanking sequence, target-site duplication, orientation, LTR state and derived substitutions. Reserve a held-out locus set before fitting.

## Analysis
1. Verify orthology from flanks, not solely internal viral homology.
2. Build observed presence/absence and shared-variant matrices.
3. Estimate ancestral-event model with loss and incomplete lineage sorting where justified.
4. Calibrate site-targeting nulls using observed viral integration preferences and genomic context.
5. Specify DFM permitted initialization features by independent function and historical-integrity constraints before comparing loci.
6. Compare likelihoods or proper predictive scores only when assumptions and datasets permit; otherwise report qualitative discriminators explicitly.
7. Perform sensitivity checks for hotspot rates, deletion rates, reference biases, shared-mutation rates and phylogenetic dependencies.

## Stop conditions
No valid independent ERV explanation if event-specific scars must be fabricated; no parity claim without held-out performance; no conflation of human-primate ancestry inference with the separate problem of evolutionary innovation.

## Output
Reproducible data manifest, scripts, figures, likelihood/prediction tables, negative results and unresolved-burden register.
