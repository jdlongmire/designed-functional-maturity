# WP-038 Training-Set Pattern Census, Rebuilt from Re-extracted Verdicts

Date: 2026-11-15. Data: data/training176-verdicts.csv (coordinate pass on the 176 non-priority training loci), data/sequence-verdicts.csv and data/reextraction-results.csv (priority 30). Method: flank-anchor geometry plus internal-anchor homology on current assemblies (hg38, panTro6, gorGor6, ponAbe3, rheMac10 chains), as in the priority pass. Macaque verdicts at coordinate level were not reliable (106 of 176 anchors unmapped; no internal-anchor check run), so macaque bits are carried from the source and flagged unverified; all macaque-absent conclusions are provisional.

## Resolution rate
Of 206 training loci, 129 have fully resolved corrected patterns (gorilla and orangutan verdicts both firm); 77 remain unresolved (chain breaks and intermediate gaps, concentrated in orangutan and in repetitive regions). **112 of the 129 resolved loci had their pattern changed by re-extraction**, almost always a source absence corrected to a presence.

## Corrected census (129 resolved loci)
| Pattern (H C G O M) | Loci | Reading |
|---|---|---|
| 1 1 1 1 0 | 120 | Present in all four apes, absent in macaque: integration in the ape stem after the macaque divergence, or an older integration lost in macaque |
| 1 1 1 0 0 | 7 | Absent in orangutan: younger integration (human-chimp-gorilla stem) or orangutan loss |
| 1 1 0 1 0 | 1 | The one surviving gorilla-absent pattern (absent-supported at coordinate level) |
| 1 1 1 1 1 | 1 | Present in all five taxa (RV15-0805, the deepest pattern in the set) |

## Event accounting, same loci, source vs corrected
- Source patterns: 153 events under single-gain accounting (129 gains + 24 losses/coincidences).
- Corrected patterns: **130 events** (129 gains + 1 loss). Independent-gain accounting also gives 130, because near-perfectly nested patterns cost one event under either accounting; the presence-level tie persists, but its meaning has changed: the second events the source data seemed to demand were measurement artifacts, not biology.
- Gorilla detail: of 113 source gorilla-absent calls among the 176, 81 are present on re-extraction, 1 absent-supported, the rest unresolved or intermediate. Orangutan detail: of 158 source-absent calls, 78 present, 8 absent-supported, rest unresolved or intermediate.

## What this establishes and what it does not
It establishes that the Retrovirology 2015 presence matrix, built on 2012 assemblies, is not a scoreable substrate: its absence calls fail at high rates against current assemblies, in the direction of under-calling presence in the non-human apes. Any published or informal argument that leans on fine-grained absence patterns from that era's assemblies inherits this problem, whichever side cites it.

It does not yet score the models. Presence patterns, even verified ones, tie between accountings by construction; discrimination still requires the joint sequence evidence (boundaries, TSD, shared derived marks, LTR divergence at alignment grade). The corrected census does change the prior landscape for that scoring: the dominant pattern in the training set is now the cleanly nested 11110, and the genuinely discordant residue is small (8 of 129 loci with a firm within-ape absence).

## Remaining gaps
77 unresolved training loci (targeted resolution via Compara alignments where chains break); macaque verification (internal-anchor pass against rheMac10); the held-out set, untouched throughout, per the unblinding rule.

## Addendum, 2026-11-15: relaxed-chain pass and macaque verification
A second pass at reduced chain stringency (liftOver minMatch 0.85, all 206 training loci, with internal anchors now also carried to macaque) is merged with the sequence verdicts in data/training206-verdicts-merged.csv. Resolution rose to 136 of 206 (124 firm, 12 provisional present-length). The firm census: 87 loci pattern 11110, **30 loci pattern 11111 with the macaque presence now verified by flank-bounded internal homology** (the source reported macaque presence at essentially none of these), 6 loci 11100, 1 locus 11010. Combined, 128 of 136 resolved loci (94 percent) are present in all four apes. Macaque verdicts are firm at 58 loci (35 present, 23 absent-supported). About 70 loci remain unresolved, concentrated in orangutan intermediate gaps and repetitive regions; the anchor method is at its limit there, and further resolution needs per-locus alignment inspection rather than more chain passes. The substantive picture from the first census is unchanged and strengthened: within-ape absence is rare and real at a handful of loci; deep presence, including into macaque, is more common than the 2015 matrix reported.

Human-Curated, AI-Enabled (HCAE)
