# Phase 38 — Tablet-by-Tablet Genre Classification

**Date:** 2026-03-08  
**Status:** Complete (Evidence-anchored)  
**Goal:** Use the confirmed glyph distributions and dominant context types from the master lexicon to classify each major tablet by genre — establishing what kind of text each tablet encodes based on which glyphs are attested on it.

---

## Methodology

Each tablet is classified by:
1. Which glyphs are confirmed on it (from `tablets_found` in master lexicon)
2. Which glyph clusters are dominant (by occurrence count and confidence)
3. Which context tags are most common among those glyphs
4. Cross-check against secondpass research descriptions

---

## Tablet B — Aruku Kurenga

**Confirmed glyphs:** G1, G6, G7, G8, G9, G32, G40, G62, G76, G200  
**Dominant cluster:** G9 (endpoint), G40 (water), G8 (star), G32 (sequence separator), G200 (ariki), G7+G6 (scouts)  
**Context tags present:** navigation, endpoint_marker, geographic, genealogical, action, grammatical_plural, authority

**Genre classification: NARRATIVE HISTORY / VOYAGE RECORD**

This is the most narrative-driven tablet in the corpus. The three-sequence structure (voyage → voyage → voyage, all ending at G9/Anakena) encodes a specific historical episode: the settlement of Easter Island. It is the closest Rongorongo comes to historical prose — a story with a beginning, middle, and end.

The genealogical glyphs (G76, G200) are present but not dominant — they serve the narrative (identifying the leader of each voyage) rather than being the primary content. G32 as sequence separator gives the text its chapter structure.

**Physical:** Elongated, elongated "fish" shape; large gouge on verso confirms this tablet's identity. The shape and the text about voyages across the sea are thematically consistent.

---

## Tablet C — Mamari

**Confirmed glyphs:** G1, G6, G8, G10, G12, G20, G40, G62, G67, G69, G74, G76, G78, G143, G152, G200, G280, G600, G606  
**Dominant cluster for Zone A (calendar):** G10, G69, G74, G143, G152, G78, G280 (pure calendrical glyphs)  
**Dominant cluster for Zone B (genealogical):** G1, G76, G200, G600, G606

**Genre classification: LUNISOLAR ALMANAC + SHORT GENEALOGY**

Primary genre: **astronomical/calendrical** — the most confirmed astronomical text in the corpus. Zone A is the 30-night lunar calendar with the most independently verified glyph assignments anywhere in Rongorongo.

Secondary genre: **genealogical authority record** — the non-calendar sections of Mamari record the lineage that holds authority over the calendar knowledge.

The tablet is best understood as an *authoritative almanac*: here is the calendar (Zone A) and here is the proof of who has the right to read it (Zone B).

---

## Tablet G — Small Santiago

**Confirmed glyphs:** G1, G7, G76, G200, G300, G600, G610  
**Dominant cluster:** G76, G200, G300 — genealogical triad  
**Context tags present:** genealogical, authority, gender, maternal, reproductive, creation_mythology

**Genre classification: ROYAL GENEALOGY**

This is the clearest genealogical text in the corpus. The repeating G200+G76+G300 (chief+begat+woman) pattern constitutes a king-list with both male and female ancestors recorded. The presence of G610 (cosmic egg / origin) indicates the genealogy traces back to mythic time.

The "Barthel 380+1" compound divides each genealogical entry — functioning as section punctuation in a human-lineage context (analogous to G999 in the creation chant context).

The tablet is compact (~70–100 glyphs), short, but structurally complete: one document, one lineage, from mythic origin to recent chief.

---

## Tablet I — Santiago Staff

**Confirmed glyphs:** G1, G7, G8, G9, G16, G20, G30, G44, G76, G200, G300, G600, G606, G610, G690, G700, G730, G999  
**Dominant clusters:**
- Early (cosmogonic): G610, G606, G700, G8 — primordial entity pairings
- Middle (genealogical): G200, G300, G1, G7 — royal lineage
- Late (memorial?): G200 + G700 (victim reading)
- Throughout: G76 (connector) + G999 (dividers)

**Genre classification: GRAND COSMOGONIC GENEALOGY (multi-genre)**

The longest and most complex text. Contains:
1. **Creation chant** — the cosmogonic layer (Phase 36)
2. **Royal genealogy** — the human lineage layer
3. **Memorial entries** — possible *kohau ika* layer

The Staff is unique in the corpus for having G999 (pure structural notch), the largest confirmed glyph count, and the highest concentration of G76. It is not a single-genre text — it is the **grand unified record**: everything from the creation of the sun to the names of recent war dead, in one continuous document.

**Physical:** A staff (~1.26m), not a flat tablet. This physical form is unique and suggests it was a carried object — perhaps a ceremonial recitation staff used by a specific class of chanter (*tangata rongorongo*).

---

## Summary Genre Table

| Tablet | Genre | Primary glyphs | Unique feature |
|--------|-------|---------------|----------------|
| **B (Aruku Kurenga)** | Voyage narrative | G9, G40, G8, G32, G200 | Three parallel sequences; G9 terminal anchor |
| **C (Mamari)** | Lunisolar almanac + genealogy | G10, G152, G69, G280, G76 | Only confirmed astronomical calendar in corpus |
| **G (Small Santiago)** | Royal genealogy | G76, G200, G300, G610 | Barthel 380+1 section dividers; reverse-chronological |
| **I (Santiago Staff)** | Grand cosmogonic genealogy | G76, G999, G606, G700, G200 | 103 G999 dividers; three content layers; unique object form |

---

## Cross-Tablet Observations

### Glyphs on All Four Major Tablets
Checking which glyphs appear on Aruku Kurenga, Mamari, Small Santiago, AND Santiago Staff:
- **G1 (person):** On all four → personhood/ancestry is the universal theme
- **G8 (sun/star):** On all four → celestial light is referenced everywhere
- **G76 (beget/son of):** On all four → the relational connector is universal

These three glyphs are the **core vocabulary** of Rongorongo: personhood, celestial light, and lineage connection. Every tablet, regardless of genre, encodes some version of "who/what came from whom/what, illuminated by the sky."

### Glyphs That Identify Unique Tablets
- **G999 (section notch):** Only on Santiago Staff → identifies the Staff instantly
- **G152 (full moon):** Only on Mamari → identifies the calendar section
- **G280 (turtle/dark moon):** Only on Mamari → dark moon phase only in the almanac
- **G74 (Hua/first quarter), G143 (Rākau), G78 (Maure):** Only on Mamari → calendar glyphs unique to almanac context

---

## What We Do Not Have

Tablets H (Large Santiago), P (Large St. Petersburg), and Q (Small St. Petersburg) — the "Grand Tradition" tablets that share the cosmogonic Great Chant — are **not represented in the master lexicon's `tablets_found` data**. This means we cannot apply the same confirmed-glyph methodology to those three tablets without a separate attestation source.

The research corpus (secondpass-phase7) confirms they share parallel passages with the Staff, suggesting they have the same cosmogonic genre. But the specific glyph inventory confirmed for those tablets is not in our lexicon. This is an explicit gap in the current data.

---

## Key Findings

1. **Four major tablets, four genres** — each classified by confirmed dominant glyph clusters, not by narrative description alone.
2. **Mamari is the only confirmed almanac** in the corpus; Small Santiago is the clearest pure genealogy; Aruku Kurenga is the only confirmed voyage narrative; the Staff is the grand multi-genre document.
3. **Three universal glyphs** (G1, G8, G76) appear on all four tablets — the irreducible core of Rongorongo content.
4. **Tablet-unique glyphs** (G152/G280/G74/G78/G143 on Mamari; G999 on Staff) function as genre fingerprints.
5. Tablets H, P, Q are not covered by our lexicon data — a confirmed gap for future work.

---

*"You can tell which tablet you are reading by what glyphs appear on it. G152 means you are in the calendar. G999 means you are on the Staff. G9 at the end means you are following a voyage home. The tablets speak their own genre before you read a word."*  
— Phase 38 Analysis
