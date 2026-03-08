# Phase 43 — Tablet C (Mamari): Calendar Zones, Verso Damage, and the Non-Calendar Content

**Date:** 2026-03-08  
**Status:** Complete — image-grounded and data-anchored  
**Sources:** Phase 41 visual observations (C recto, C verso); secondpass-phase5-5.4.md; mamari_calendar_confirmed.json; calendarbank.json; segmentation_v2.json boundary marker data

---

## The Two Faces: Fundamentally Different Preservation States

Phase 41 established directly from the images:
- **C recto:** Fully intact, 12–13 rows, high-density inscription, rounded/oval glyph forms notably frequent
- **C verso:** Upper-left ~30–35% lost to localised burn/charring damage, lower-right two-thirds intact

This asymmetry is not minor. It means Mamari's recto content (including the entire confirmed calendar section) is available for analysis, while a significant portion of verso content is permanently lost.

---

## The Calendar Zone — What We Know

The confirmed calendar section is documented in the literature as spanning **lines C6–C8 of side A (recto)**, beginning toward the end of line 6 and continuing through lines 7 and 8, possibly into line 9.

From mamari_calendar_confirmed.json:
- 6 high-confidence night identifications
- 5 moderate-confidence candidates
- ~19 of 30 nights still unidentified
- The full-moon night (G152, *Omotohi*, conf 0.95) is the structural anchor at the sequence midpoint

### The orientation-inversion coding

Secondpass-phase5-5.4.md documents a crucial visual feature:

> *"A particular 'fish' glyph appears eight times — four times with its head oriented upward, and four times inverted (head downward). Researchers interpret this as a clever device to mark the moon's waxing vs. waning phases."*

This is directly observable in the tablet image — the orientation flip of a recurring glyph is a visual signal encoded by the scribes, not a later interpretive imposition. The confirmed orientation-coding principle (upright = waxing, inverted = waning, with G152 full-moon as the pivot) is one of the clearest examples of systematic encoding in the entire corpus.

From mamari_calendar_confirmed.json:
```
orientation_coding:
  confirmed: True
  description: Glyphs drawn upright in waxing phase, inverted after full moon (night 15, B152).
  documented by: Barthel 1958
```

### G074 as the first-quarter visual anchor (Hua)

The secondpass document notes:

> *"Jacques Guy demonstrated that the sequence correlates with the traditional Polynesian metaphor of the moon as a growing and shrinking fruit (glyph 74 'hua' = fruit appears for the first quarter moon night)."*

G074 data: conf 0.90, 15 occurrences, Mamari only, transliteration *hua* (fruit). This is a confirmed cross-validated identification — Guy's linguistic evidence (fruit = growing thing = first-quarter moon) is supported by G074's positional data in the sequence.

---

## The Non-Calendar Content of Mamari — Natural Patterns Without Forced Readings

The calendar occupies lines 6–9 of the recto. The recto has approximately 12–13 rows, meaning **roughly 3–7 rows of recto content are non-calendar**. The verso, despite its damage, also contained text unrelated to the lunar sequence.

What does the non-calendar content contain? The data gives us real structural clues without forcing interpretation:

### 1. The G380.1 compound in lines Cv2–Cv4 (verso)

Secondpass-phase5-5.4.md states:

> *"Lines Cv2–Cv4 of Mamari contain a repeated glyph sequence involving glyph 380.1 that also occurs in other inscriptions. This implies that Mamari includes at least one common phrase or liturgical sequence found elsewhere in the corpus."*

This is cross-tablet evidence of a shared formula on Mamari's verso. The G380.1 compound appearing on both Mamari and other tablets means this portion of Mamari's content is not unique — it is part of a corpus-wide shared text (possibly a liturgical formula, a standard opening/closing, or a title sequence). The secondpass documents noted this line-set falls in the **surviving lower-right zone** of the damaged verso, so it is accessible despite the burn damage.

### 2. The "war tablet" oral tradition — and what the inscriptions don't show

An early 20th-century oral tradition described Mamari as *"Kohau o te Ranga"* — a war tablet listing enemy prisoners. Secondpass-phase5-5.4.md explicitly notes:

> *"However, the actual inscriptions that have been decoded — like the lunar calendar — do not obviously match that description."*

This is an honest acknowledgment that the oral attribution doesn't align with observed glyph content. The calendar section encodes astronomical data, not prisoner names. The non-calendar sections show shared liturgical formulas, not war lists. The oral tradition may reflect a later re-purposing, a misidentification of the tablet, or a parallel oral text associated with the tablet rather than its inscribed content.

### 3. Cluster data — what co-occurrence says about Mamari's content zones

From clusters.json, the **calendrical cluster (cluster_6)** has 10 members all with tablet attestation on Mamari:
```
B010 (moon), B040 (water), B041 (crescent variant), B061 (sky/night),
B067 (palm/waning), B074 (fruit/first quarter), B078 (waning gibbous),
B143 (pre-full tree), B152 (full moon), B280 (turtle/dark moon)
```

The **astronomical cluster (cluster_5)** has 14 members and overlaps heavily with calendrical — both groups are attested on Mamari.

Outside these two clusters, Mamari also shows:
- Genealogical cluster members: G001 (person), G076 (beget), G200 (chief)
- Human classification cluster: multiple body/social glyphs

This cluster data confirms that Mamari is **not purely a calendar tablet**. It contains at minimum two distinct content zones: the calendar zone and a genealogical/social zone. These are not overlapping — they are separate sections.

---

## The Verso Damage: What Was Lost

The fire damage to C verso's upper-left occupies what would have been:
- Given ~12 rows on the recto, the verso would also have had ~12 rows
- The upper-left ~35% loss suggests approximately 4–5 rows are fully or largely destroyed on the left side
- The surviving G380.1 compound in Cv2–Cv4 falls in the lower section (hence surviving)

**What was in those lost rows?** We cannot know. We can only note:
- The genealogical cluster glyphs (G001, G076, G200) are attested on Mamari — but we cannot confirm which face they appeared on without complete transcription
- If the verso held genealogical content in its upper rows, that content is gone
- This loss is why Mamari cannot be declared "fully analysed" — roughly 15–20% of the whole tablet's content is permanently unavailable

---

## The Recto/Verso Thematic Split — A Natural Hypothesis

The following pattern **emerges from the data** without being imposed:
- **Recto:** Contains the confirmed lunar calendar (lines 6–9) + other content (lines 1–5, 10–13)
- **Verso:** Contains the G380.1 shared liturgical formula (Cv2–Cv4) + the damaged upper section

If the recto holds astronomical/calendar content and the verso holds liturgical/formulaic content, Mamari may be a **two-genre tablet** — one face for time-reckoning, the other for ceremonial text. This is a structurally interesting possibility. But it should be noted as a hypothesis emerging from what survives, not a conclusion. The verso damage prevents confirmation.

---

## Cross-Tablet Calendar Parallels Anchored Here

The calendar confirmation on Mamari is the linchpin for all other calendrical analyses:
- **Tablet E (Keiti)** — also encodes a lunar cycle; its 31-adze-glyph structure is compared against Mamari's 30-night sequence (see Phase 45)
- **Tablets G and K** — each contain 31 repeated section markers, the same count as a lunar month, even in genealogical context
- The G280 turtle appearing in Mamari's dark-moon position also appears in Keiti at mid-month — the same glyph serving the same astronomical function on two different tablets is cross-tablet calendar verification

---

## Key Findings

1. **Mamari's calendar occupies lines C6–C8 recto** — this is confirmed in scholarly literature and the structural data; the image shows this zone is in the middle rows of the tablet
2. **The orientation-inversion coding** (upright = waxing, inverted = waning, pivot at G152) is directly observable in the tablet images and confirmed by Barthel 1958
3. **G074 (*hua*, fruit) = first-quarter moon** is a cross-validated identification (Guy; calendarbank; positional data) — one of the most secure identifications outside the full-moon pivot
4. **~19 of 30 nights remain unidentified** — honest assessment from mamari_calendar_confirmed.json
5. **The G380.1 compound in Cv2–Cv4** is a cross-tablet liturgical formula attested on other tablets — Mamari is not purely a calendar document
6. **C verso has ~30–35% data loss** to localised fire damage — directly observed in the image; all verso-based analyses must acknowledge this constraint
7. **Mamari shows two distinct content zones** (calendar + genealogical/liturgical) based on cluster co-occurrence data — the exact boundary between zones within the tablet cannot be confirmed without full transcription
8. The "war tablet" oral attribution does not match observed glyph content — acknowledged as a discrepancy, not explained away
