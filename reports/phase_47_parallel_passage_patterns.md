# Phase 47 — The Six Parallel Passage Patterns: Cross-Tablet Formula Confirmation

**Date:** 2026-03-08  
**Status:** Complete — parallel_passages.json v1+v2 data-grounded  
**Sources:** parallel_passages.json (v1: 6 patterns, 42 total occurrences); parallel_passages_v2.json (4 patterns with visual verification notes); secondpass documentation

---

## What Parallel Passages Are and Why They Matter

A parallel passage is a glyph sequence that appears in substantially the same form on **more than one tablet**. Because each tablet was likely produced independently, the same sequence appearing on multiple tablets is strong evidence that:
1. The sequence encodes a conventional, standardised phrase or formula
2. The phrase was well-known enough to be copied or independently reproduced across different scribal traditions
3. Its meaning is more constrained than a unique sequence (less ambiguity: if you see the same pattern in the same position on 4 tablets, its function is narrowed)

v1 documents **6 patterns** across 42 total occurrences. v2 refines 4 of these with image verification notes.

---

## Pattern 1: Genealogical Formula (B001-B076-B001)

**Tablets:** H (Santiago Staff), G (Small Santiago), K (Small London), B (Aruku Kurenga)  
**Glyph sequence:** B001 – B076 – B001  
**Confidence:** 0.90 | **Occurrences:** 15 | **Variability:** low  
**Alignment score:** 0.92

**What the sequence contains:**
- B001 = person/tangata (conf 0.85, 127 occ)
- B076 = beget/copulate/'ai (conf 0.95, 34 occ)
- B001 = person/tangata again

The pattern X – B076 – Y appears 15 times across four tablets. The two flanking glyphs are not always identical B001 figures — they can be any person-type glyph — but the central B076 is constant.

**What this pattern does on its own terms (without forcing a reading):** A person-type glyph, then B076 (which lexically and contextually means begetting/procreation), then another person-type glyph. The middle glyph links the two flanking persons. The structural analogy is straightforward: A [link] B = A is connected to B through B076's action.

**Why this is a formula and not coincidence:** 15 occurrences across 4 tablets, all with low variability and 0.92 alignment score. This is one of the highest-frequency, highest-consistency patterns in the corpus.

---

## Pattern 2: Lunar Cycle (B152-series)

**Tablets:** C (Mamari only)  
**Glyph sequence:** The complete B152-anchored sequence  
**Confidence:** 0.98 | **Occurrences:** 1 (single unique text) | **Variability:** none  
**Alignment score:** 0.98

This is the confirmed Mamari calendar. It has the highest confidence (0.98) and zero variability — because it is a unique sequence on a single tablet. "Parallel passage" here means the internal structure is so consistent that it functions as a self-corroborating text rather than requiring cross-tablet comparison for confirmation.

**Cross-tablet calendar linkage:** While P002 itself is unique to Mamari, it cross-links to P006 (astronomical markers on Mamari and Tablet A) and to the structural parallels identified on Tablet E (Keiti) in Phase 45.

---

## Pattern 3: Procreation Formula (NAME-B076-NAME)

**Tablets:** H (Santiago Staff), G (Small Santiago)  
**Glyph sequence:** NAME – B076 – NAME  
**Confidence:** 0.88 | **Occurrences:** 8 | **Variability:** low  
**Alignment score:** 0.88

This pattern is a variant of P001. Where P001 uses generic B001 (person) on both sides of B076, P003 uses what appear to be specific *named* figures — more differentiated person-glyphs that the lexicon associates with specific named individuals.

The distinction P001 vs P003:
- P001: generic X [begets] generic Y
- P003: named X [begets] named Y → produces named Z

P003's third element (the Z in the formula) is noted in secondpass documents as B400 (offspring/young, conf 0.65) — the child produced by the procreation event. This creates a **three-element formula:**

```
PARENT_A  +  B076  +  PARENT_B  =  CHILD (B400)
```

The procreation-chain formula found 8 times on the Santiago Staff and Small Santiago is the core of Fischer's proposed genealogical reading of the Staff — though Fischer's specific phonetic assignments to the named glyphs remain disputed, the **structural formula itself** (two named figures + B076 = offspring) is confirmed by the 8-occurrence, 0.88-confidence parallel passage data.

---

## Pattern 4: Title Sequence (B200-NAME)

**Tablets:** B (Aruku Kurenga), H (Santiago Staff), G (Small Santiago)  
**Glyph sequence:** B200 – NAME  
**Confidence:** 0.85 | **Occurrences:** 12 | **Variability:** moderate  
**Alignment score:** 0.85

B200 (ariki/chief, conf 0.95) preceding a personal-name cluster. Variability is "moderate" — the NAME element varies between instances (different chiefs = different name glyphs) while B200 is constant.

This is the **title formula** — how the script marks a titled individual. The chief-glyph appearing before a name-cluster signals: "the following glyph(s) identify a specific chief."

**Cross-tablet confirmation of Tablet D analysis (Phase 44):** Line a3 of Tablet D contains repeated B200 occurrences. The parallel passage data confirms B200-NAME is a standard formula on B, H, and G. The same formula on D is not a local scribal quirk but a corpus-wide convention.

---

## Pattern 5: Bird Enumeration (B600-series)

**Tablets:** H (Santiago Staff only)  
**Glyph sequence:** B600-series  
**Confidence:** 0.85 | **Occurrences:** 1 (single instance) | **Variability:** low  
**Alignment score:** 0.90

A systematic bird catalog on the Santiago Staff. The high alignment score (0.90) reflects internal consistency (the bird sequence is structurally regular) even though it only appears on one tablet.

This is the "bird enumeration" documented in secondpass analyses of the Santiago Staff — a section where multiple bird glyphs appear in sequence, interpreted as a systematic listing of avian species or ritual bird associations.

**Significance:** The Santiago Staff's bird section is a **different genre** from its genealogical sections. A genealogy doesn't enumerate bird species. The bird catalog section demonstrates the Staff contains multiple distinct content types — not a single continuous genealogy.

---

## Pattern 6: Astronomical Markers

**Tablets:** C (Mamari), A (Tahua)  
**Glyph sequence:** astronomical-cluster  
**Confidence:** 0.75 | **Occurrences:** 5 | **Variability:** moderate  
**Alignment score:** 0.82

Astronomical/star observation markers appearing on both Mamari and Tablet A (Tahua). This is the least confirmed pattern — moderate confidence, 5 occurrences, moderate variability.

**Significance:** Tablet A (Tahua) is listed in the corpus as having astronomical content that parallels Mamari. If P006 is confirmed, it means Mamari's astronomical content is not unique — at least one other tablet records celestial observations using similar glyph clusters. Tablet A's astronomical content has not been individually analysed in phases 1–45 and warrants dedicated attention.

---

## Aggregate Statistics

| Metric | Value |
|--------|-------|
| Total parallel sequences identified | 6 |
| Cross-tablet confirmations | 13 |
| Patterns unique to one tablet | 2 (P002 lunar, P005 bird enum.) |
| Multi-tablet patterns | 4 |
| Average alignment score | 0.892 |
| Total occurrences across all patterns | 42 |

The 0.892 average alignment score across all patterns is high. It means that when the same glyph sequence appears on multiple tablets, it appears with ~89% structural similarity — not identical (which would be copying), but close enough to confirm a shared template.

---

## What the Patterns Collectively Confirm

1. **The corpus is not a random collection of independent texts.** Four out of six patterns span multiple tablets. A shared formulaic vocabulary exists.

2. **B076 is a relational operator**, not just a content glyph. Its appearance in both P001 and P003 — as the central connector in genealogical formulas — confirms its grammatical function. This is the most structurally supported functional-glyph assignment in the corpus.

3. **B200 + NAME is a title formula** confirmed on three tablets. Any glyph sequence beginning with B200 on any tablet is most parsimoniously read as "chief [X]."

4. **The Santiago Staff has multiple content types** — at minimum, genealogical (P001, P003, P004) and avian-catalog (P005). It is not a single-genre document.

5. **Mamari's calendar is confirmed unique** — P002 occurs only on C. No other tablet replicates the full 30-night sequence. But the calendar system itself is not unique — Keiti (Phase 45) independently encodes the same lunar system.
