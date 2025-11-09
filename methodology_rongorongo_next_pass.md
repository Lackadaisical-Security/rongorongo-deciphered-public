# Rongorongo Multi-Prong Research Methodology (Next Pass · Phase Map)

**Maintainer:** Lackadaisical Security (Operator & Spectre)  
**Lineage:** Universal Methodology → Byblos / Linear A / Indus branches → **Rongorongo-tailored**  
**Scope:** End-to-end, reproducible pipeline for a second/third research pass with **15–20 phases**.  
**Core doctrine:** evidence-first; natural pattern emergence; never force interpretations; **never discard** “misfits”—quarantine them until refuted; expect **3–5 senses per glyph** on average; meaning before full translation; culture/history/Polynesian influence resolve the rest.

---

## 0) Ground Rules (apply to all phases)

- **Reproducible**: Every phase emits machine-readable artifacts + seeds (`run.json`).
- **Variant-preserving**: No silent collapses; ligatures remain composite.
- **Multi-sense aware**: Each glyph may map to **SenseBank** entries (3–5 typical).
- **Falsifiable**: Each claim carries tests, baselines, & confidence.
- **Quarantine**: Misfits go to `/sandbox/quarantine` with reasons; never deleted.
- **No speculation**: Cross-linguistic cues are constraints/filters, not targets.
- **File hygiene**: Checksums for inputs/outputs; changelog per run.

---

## Repository Layout (stable across phases)

```
/inputs
  /images/               # high-res TIF with SHA256
  /transcriptions/       # per edition (Barthel/Fischer/Pozdniakov/…)
/corpus
  /normalized/           # lossless JSON lines w/ variants, ligatures
  /variants/             # variant maps, ligature decompositions
  /parallels/            # alignments (NW/SW) & scores
/banks
  sensebank.json         # glyph → {senses[]} multi-meaning entries
  motifbank.json         # recurring sequences & contexts
  namebank.json          # personal/toponym candidates
  calendarbank.json      # lunar/month/day candidates
  numeralbank.json       # numeral hypotheses & tests
/analysis
  freqs_ngrams.csv
  entropy.tsv
  cooccur.gexf
  clusters.json
  constraints.json
  segmentation.jsonl
/reports
  phase_##_*.md
  claims/                # external theory audits (defer until base is solid)
/runs
  YYYYMMDD_HHMMSS/run.json
/licenses
  ghost_license_v1.md
  ancient_scripts_attribution_license_v1.md
```

---

# Phases Overview (18 total)

Each phase includes: **Goal · Inputs · Method · Outputs · QA/Exit**.

---

## Phase 1 — Corpus Assembly & Provenance Hardening
**Goal:** Assemble a *lossless*, attested corpus; lock provenance.

- **Inputs:** images, per-edition transcriptions, prior JSONs (datasets.zip / rongorongo-research.zip / latest lexicon).  
- **Method:** Build `sources.yaml`; index tablets, sides, lines, orientation hints; hash all files.  
- **Outputs:** `/corpus/normalized/*.jsonl` (one line = one line of text + tokens + provenance), `sources.yaml`.  
- **QA/Exit:** 100% of lines present; hashes recorded; edition coverage matrix saved.

---

## Phase 2 — Variant & Ligature Discipline
**Goal:** Preserve originals, model relationships without collapse.

- **Inputs:** normalized JSONL, edition glyph IDs.  
- **Method:** Create `variants.csv` (canonical↔variant), `ligatures.csv` (parts[]). Keep ligatures as composite tokens; optional surrogate **only for stats**.  
- **Outputs:** `/corpus/variants/{variants.csv, ligatures.csv}`, `constraints.json` (do-not-split rules).  
- **QA/Exit:** Round-trip check: decomposed → recomposed equals source within tolerance.

---

## Phase 3 — Orientation & Line Topology Resolution
**Goal:** Encode correct reading orders per **line** (not tablet).

- **Method:** Heuristics + visual cues + prior notes; assign `reading_order`, `confidence`.  
- **Outputs:** Updated lines with `reading_order`, topology metadata.  
- **QA/Exit:** Blind spot audit: ≤5% lines flagged “uncertain”; ambiguity tracked.

---

## Phase 4 — Statistical Spine (Freqs, Entropy, N-grams)
**Goal:** Quantify structure.

- **Method:** Unigram/bigram/trigram; block entropy (n=1..8); Zipf fit; start/end positional stats.  
- **Outputs:** `/analysis/freqs_ngrams.csv`, `entropy.tsv`, start/end bias report.  
- **QA/Exit:** Repro under different seeds; nulls (shuffle/Markov) computed.

---

## Phase 5 — Co-Occurrence Graphs & Community Detection
**Goal:** Discover natural clusters (topics/functions).

- **Method:** Windowed co-occurrence → weighted graph; Louvain/Leiden; stability via bootstraps.  
- **Outputs:** `/analysis/cooccur.gexf`, `clusters.json` (membership, modularity, stability).  
- **QA/Exit:** Clusters stable (≥0.7 Jaccard across bootstraps); hubs identified.

---

## Phase 6 — Parallels & Alignment Atlas
**Goal:** Map repeated passages.

- **Method:** NW/SW alignments over token IDs; export matched spans, scores, heatmaps.  
- **Outputs:** `/corpus/parallels/parallels.csv`, exemplar PNGs (optional).  
- **QA/Exit:** Manual spot-checks on top 20 alignments; false-match rate reported.

---

## Phase 7 — Segmentation (Words/Phrases) without Spaces
**Goal:** Propose boundaries conservatively.

- **Method:** CRF/HMM + constraints (no splitting ligatures; honor high-affix candidates); use positional/cluster cues; evaluate on held-out lines.  
- **Outputs:** `/analysis/segmentation.jsonl` (boundaries + confidence).  
- **QA/Exit:** Improves bigram→trigram predictability vs. nulls; error bands logged.

---

## Phase 8 — Motif Discovery & Ledger
**Goal:** Catalog recurrent sequences with context.

- **Method:** Mine repeated n-grams under boundary penalties; group by parallel support; rank by support & cross-tablet spread.  
- **Outputs:** `/banks/motifbank.json` (motif_id, parts, support, tablets, exemplars, evidence_grade).  
- **QA/Exit:** Only motifs with ≥2 independent contexts promoted; grades (A–D) assigned.

---

## Phase 9 — Multi-Sense Modeling (SenseBank)
**Goal:** Model **3–5 meanings per glyph** as first-class citizens.

- **Method:** For each glyph: propose `senses[]` with **evidence vectors** (freq/position/cluster/motif/parallel/cultural); weight via logistic or Bayesian update; allow overlaps.  
- **Outputs:** `/banks/sensebank.json`:
  ```json
  {
    "glyph":"B006",
    "senses":[
      {"id":"plural/collective","evidence":{"freq":0.9,"position":0.7,"motif":0.8}, "confidence":0.88},
      {"id":"hand/action","evidence":{"iconic":0.5,"context":0.4}, "confidence":0.52}
    ]
  }
  ```
- **QA/Exit:** Conflicts flagged; no forced pruning—mark as competing senses with priors.

---

## Phase 10 — Constraint-Only Polynesian/Linguistic Filters
**Goal:** Use language facts as *filters*, not targets.

- **Method:** Polynesian phonotactics (CV bias, vowel endings), known Rapa Nui calendars/kinship sets; reject sequences that violate hard constraints; never back-fit.  
- **Outputs:** `constraints.json` (accepted/rejected patterns with reasons), filtered candidate lists.  
- **QA/Exit:** Report filter impact; ensure no single filter eliminates >10% of attested data.

---

## Phase 11 — Named Entities & Onomastics (NameBank)
**Goal:** Isolate personal/toponymic strings.

- **Method:** Identify repeated multi-glyph blocks in genealogical contexts; boundary patterns with “connector” motifs; cluster by co-occurrence and position.  
- **Outputs:** `/banks/namebank.json` (string, contexts, tablets, exemplars, confidence).  
- **QA/Exit:** Recurrence across ≥2 contexts or tablets; connector-adjacency verified.

---

## Phase 12 — Calendrics & Cycles (CalendarBank)
**Goal:** Extract lunar/month/day systems without forcing.

- **Method:** Detect ~30-cycle motifs; cross-check spacing & phase order; map candidate night/day names as **senses**, not fixed readings.  
- **Outputs:** `/banks/calendarbank.json` (cycle motifs, anchors, alternatives).  
- **QA/Exit:** Cycles survive hold-out; alternatives preserved where ambiguous.

---

## Phase 13 — Numeral System & Quantification
**Goal:** Identify counting patterns and numeric morphemes.

- **Method:** Search for monotonic subsequences, tally contexts (lists, counts); test bases (5/10/20); simulate readings and compare against frequency deltas.  
- **Outputs:** `/banks/numeralbank.json` (hypotheses, evidence, counter-evidence).  
- **QA/Exit:** Must beat Markov null on prediction of counted lists; ambiguity retained.

---

## Phase 14 — Proto-Grammar: Affixes, Particles, Order
**Goal:** Draft function classes (no hard decoding yet).

- **Method:** Classify high-freq glyphs by positional behavior (suffix-like, initial-like, clitic-like); test alternation classes (e.g., CV alternation as constraint).  
- **Outputs:** `proto_grammar.json` (classes, rules, exceptions, tests).  
- **QA/Exit:** Rules must improve model perplexity on held-out lines and remain tablet-agnostic.

---

## Phase 15 — Cross-Validation & Robustness
**Goal:** Stress-test everything.

- **Method:** K-fold across tablets/lines; bootstrap resamples; perturb variant handling; re-score motifs, senses, grammar.  
- **Outputs:** `robustness_report.md`, deltas per artifact.  
- **QA/Exit:** No key metric swings >15% under perturbations unless flagged.

---

## Phase 16 — Cultural/Context Integration (Evidence-Bound)
**Goal:** Bring in archaeology, oral history, myth **only** as corroboration.

- **Method:** Link motifs to culture frames (genealogy, ritual, agriculture, voyages). Keep as **ContextFrames** with citations; never override data.  
- **Outputs:** `context_frames.json` (frame → supporting motifs/lines).  
- **QA/Exit:** Every link shows at least two internal evidences + one external context.

---

## Phase 17 — Synthesis & Sense-Weighted Readings
**Goal:** Produce **meaningful** line glosses (not full translations).

- **Method:** For each line: choose best-supported **sense** per glyph; emit **sense-gloss** with alternates; highlight uncertain spans.  
- **Outputs:** `/reports/phase_17_sense_glosses.md` + machine JSON for UI.  
- **QA/Exit:** Coverage ≥70% of tokens with confidence ≥0.6; alternates preserved.

---

## Phase 18 — External Claim Harness (Deferred Audits)
**Goal:** Neutral audits once base is solid.

- **Method:** `make audit CLAIM=<slug>` runs pre-registered tests (parallel consistency, cross-tablet transfer, entropy/fit vs. nulls, variant-robustness).  
- **Outputs:** `/reports/claims/audit_<slug>.md` + scorecard JSON.  
- **QA/Exit:** Claims **pass/fail/partial** with concrete counter-examples; no rhetoric.

---

## Phase 19 — Packaging & Release Engineering
**Goal:** Ship clean, reproducible research drops.

- **Method:** Snapshot `/runs/*`, freeze seeds; export CSV/JSON + minimal figures; sign checksums; include licenses.  
- **Outputs:** `rongorongo_phase_##_release.zip` (corpus, banks, analyses, reports).  
- **QA/Exit:** Fresh clone + `make all` reproduces hashes.

---

## Phase 20 — Roadmap to Translation (Post-Meaning)
**Goal:** Lay out the bridge from **sense-level** to **text-level** translation.

- **Method:** Identify highest-confidence tablets/segments; propose phased decoding plan (names → calendars → ritual formulas → narratives).  
- **Outputs:** `/reports/phase_20_translation_roadmap.md`.  
- **QA/Exit:** Milestones have measurable gates (e.g., % sense coverage, grammar test thresholds).

---

# Key Data Structures (quick refs)

### Normalized Line (JSONL)
```json
{
  "tablet_id":"C_Mamari","side":"recto","line_id":"C-r1",
  "reading_order":"reverse-boustrophedon","confidence":0.92,
  "tokens":[
    {"t":"glyph","id":"B102","edition":"Barthel","bbox":[...]},
    {"t":"ligature","parts":["B326","B45"],"bbox":[...]}
  ],
  "provenance":{"image_sha256":"…","source_id":"…","editor":"…"}
}
```

### SenseBank (multi-meaning)
```json
{
  "glyph":"B300",
  "senses":[
    {"id":"female/woman","contexts":["genealogy"],"evidence":{"cluster":0.71,"parallel":0.63},"confidence":0.75},
    {"id":"mother","contexts":["genealogy"],"evidence":{"motif":0.68},"confidence":0.62}
  ],
  "notes":"Senses coexist; choose per context at inference time."
}
```

### MotifBank
```json
{"motif_id":"M0017","parts":["Bxxx","Byyy","Bzzz"],"support":19,
 "tablets":["A","C","E"],"grade":"A",
 "exemplars":[["A-r2",14,16],["C-r1",3,5]]}
```

---

# Quality Gates & Tests (used across phases)

- **Hold-out generalization:** Train on X, test on Y/Z; require ΔF1 / perplexity drop beyond shuffled & Markov nulls.  
- **Parallel consistency:** Aligned spans must preserve sense assignments (≤k edit distance on sense strings).  
- **Variant robustness:** Results stable under variant merges/splits.  
- **Effect sizes over p-values:** Always report both, prefer effect sizes for decisions.  
- **Misfit registry:** Every rejected/odd pattern logged with reason & re-check schedule.

---

# QuickStart Runbook (for this pass)

1. **Phase 1–3**: Normalize, variants/ligatures, orientation.  
2. **Phase 4–6**: Stats spine, co-occur clusters, parallels.  
3. **Phase 7–8**: Segmentation + motif mining; seed MotifBank.  
4. **Phase 9–14**: SenseBank (multi-sense), filters, names, calendars, numerals, proto-grammar.  
5. **Phase 15–16**: Robustness & culture frames (evidence-bound).  
6. **Phase 17**: Sense-weighted glosses.  
7. **Phase 18–19**: (Later) external audits, packaging.  
8. **Phase 20**: Translation roadmap.

---

## Notes for the Team

- We **opt for meaning** (sense-level) first; full translation emerges where culture + structure + context converge.  
- Keep *all* alternates alive; let usage and tests promote/demote, not taste.  
- If something “doesn’t fit,” tag it, quarantine it, and schedule a re-test—**never throw it away**.  
- Expect **3–5 senses per glyph**; design UI/scripts to pick senses per context automatically, with human override.
