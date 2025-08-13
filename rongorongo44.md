| Why the staff?                                                                                                                                                                                                                                                                                             | How we exploit it                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *a)* ≈2 300 glyphs – the largest single dataset.  <br>*b)* Explicit **segment dividers** (the vertical bar, normally catalogued as glyph 999) break the text into ≈100 clearly bounded units.  <br>*c)* A single glyph (76, the phallic/patronymic sign) recurs > 560 times – a strong statistical handle. | 1. Create a clean digital transcription (normalise ligatures, orientation, allographs).<br>2. Slice the text at every 999 divider; compute segment length distribution (it is usually 3 or 6 glyphs).<br>3. For each segment, log which glyph carries the 76 suffix and what follows it.<br>4. Generate two parallel working glosses for every segment:  <br> • **Genealogy gloss**  “X, child-of Y” …  <br> • **Cosmogonic gloss**  “X copulated-with Y; Z resulted.”<br>5. Feed both gloss sets into a database so every later tablet we study can be checked automatically against them. |

*Deliverable 1:* a spreadsheet where every staff segment is coded, counted and has both tentative readings attached.

---

## 2 Cross-link the staff to its closest parallel – Aruku Kurenga (Tablet B)

Tablet B contains three almost-identical blocks, generally taken to map the *Hau-Maka / scouts / Hotu Matuʽa* three-voyage legend.

1. Mark the **32 delimiter** that precedes each block; copy the three blocks into three rows of a comparative table.
2. Align them column-wise; highlight fixed vs. varying glyphs.
3. Where a Staff triplet matches Tablet B, copy our two candidate glosses across; note which gloss (“genealogy” or “cosmogony”) produces the more coherent narrative of the voyage legend.
4. Flag any glyph that always swaps orientation or is doubled – likely plural or grammatical markers; update the master lexicon accordingly.

*Deliverable 2:* a colour-coded alignment showing which staff segments re-appear on Tablet B and how each hypothesis copes with them.

---

## 3 Anchor the lexicon with the one universally accepted text – the Mamari lunar calendar

*Lines Ca6 – Ca8* of Mamari give us 30 consecutive nights of the Rapa Nui lunar month.

1. Lock in high-confidence values:
    • glyph 10 = *mahina* “moon / night”;
    • glyph 152 = “full moon / complete”;
    • orientation-flip of the fish glyph separates waxing from waning.
2. Harvest every other tablet line that repeats those crescent-based clusters; see whether they function as calendars, date stamps or rhetorical “time passes” markers.
3. Add every secure value to the lexicon with confidence scores; tag them “calendrical-confirmed”.

*Deliverable 3:* an updated lexicon file (with confidence tags) and a cheat-sheet of reliably read glyphs for quick reference.

---

## 4 Normalise the sign inventory and build corpus-wide N-gram statistics

1. Run clustering on Barthel’s ≈400 numbered shapes; merge allographs and detachable affixes until we reach the ≈50–60 “core” signs most analyses predict.
2. Compute bigram/trigram frequencies for the whole corpus; highlight sequences that are:
    • staff-specific  → likely genre markers;
    • cross-tablet   → formulae worth targeting next;
    • unique one-offs → probable proper names.

*Deliverable 4:* a frequency report and an interactive graph showing which tablets share which recurrent phrases.

---

## 5 Test the rival macro-hypotheses head-to-head

| Question                                     | Genealogy model predicts                                                  | Cosmogony model predicts                                                        |
| -------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Distribution of glyph 76 outside the staff   | Rare; concentrated in genealogical lists only.                            | Moderately common in all mythic texts.                                          |
| Presence of fish glyph 700 in staff segments | Clusters where we already see warfare or “victim” lists on other tablets. | Appears whenever a marine “mother” figure mates, regardless of genre.           |
| Segment order on staff                       | Can match known king/ancestor lists if read bottom-to-top.                | Follows a mythological element-creation progression (sky → earth → sun → etc.). |

For every prediction, pull the actual counts from Deliverable 4; score which hypothesis explains more of the data.  Keep the losing hypothesis alive only where it still fits un-explained pockets.

---

## 6 Iterate: feed results back into the lexicon and re-run alignments

Every time a glyph’s confidence passes a threshold (say ≥ 0.7), propagate that value through:

* the staff spreadsheet → may unlock neighbouring unknowns;
* the Aruku Kurenga alignment → tightens voyage narrative;
* the N-gram mesh → may reveal further parallel passages to harvest.

---

## 7 Bring in external cultural data last, not first

* Ethnographic place-lists, king lists, and the *Atua Matariri* chant\* are powerful checks—but only **after** the internal patterns have suggested a translation.
* When a proposed reading names a place or person, verify that the glyph shape also works as a pictorial/rebus match (e.g., bird glyph 600 plausibly standing for the motu-islets in the scouts’ circuit).

---

## 8 Publish tools & data for peer replication

*Release:*

* clean Unicode-style transcript files;
* Python notebooks for every statistics step;
* side-by-side PDF plates with segment divisions and tentative glosses.

Crowd-sourced cross-checking is invaluable when working with such a tiny corpus.

---

### Expected milestones & timeline (approx.)

| Month | Milestone                                                                        |
| ----- | -------------------------------------------------------------------------------- |
| 1     | Deliverables 1 & 3 (staff spreadsheet; confirmed calendar set).                  |
| 2     | Deliverable 2 (Aruku alignment) + first lexicon update.                          |
| 3     | Deliverable 4 (sign-inventory reduction & N-gram map).                           |
| 4     | First full score-card: genealogy vs cosmogony.  Revise plan accordingly.         |
| 6     | Public release of data/tools; workshop with Polynesian linguists for fresh eyes. |

---

## Why this plan is worth the effort

* **Transparent:** every inference is traceable back to counts, not gut feeling.
* **Incremental:** we bank each small certainty (calendar nights, obvious plural markers, etc.) instead of waiting for a miraculous “key.”
* **Falsifiable:** competing readings are set up so the corpus itself can decide between them.
* **Culturally grounded:** external myths are used as *tests*, never as axioms—guarding us against circular argument.

Follow the steps above and, even if a full phonetic decipherment remains elusive, we will have:

* the cleanest corpus ever assembled,
* a high-confidence core lexicon, and
* a demonstrably better grasp of what every major tablet is *about*—history, calendar, cosmology, or all three woven together.

That, in turn, is the solid platform future scholars will need for the final breakthrough.
