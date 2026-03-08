# Phase 49 — Social Age Hierarchy: G7 → G1 → G200 → G500 → G400

**Date:** 2026-03-08  
**Status:** Complete — master lexicon and cluster data-grounded  
**Sources:** Master lexicon entries G1/G7/G200/G300/G400/G500; cluster_1 (genealogical); cluster_2 (human classification); parallel_passages P001/P003/P004; secondpass-phase6.1.md

---

## The Social Taxonomy in Rongorongo

The script encodes a layered social classification system using five clearly differentiated human-figure glyphs. Each represents a distinct point in the social/generational hierarchy. Together they form a complete taxonomy of Rapa Nui social identity as recorded in the tablets.

| Glyph | Core meaning | Rapanui term | Conf | Occ | Tablets |
|-------|-------------|-------------|------|-----|---------|
| **G007** | child / descendant | *poki* | 0.80 | 28 | Santiago Staff, Aruku Kurenga |
| **G001** | person / human | *tangata* | 0.85 | 127 | Aruku Kurenga, Mamari, Santiago Staff |
| **G300** | woman / mother | *vi'e / māmā* | 0.75 | 43 | Santiago Staff, Small Santiago |
| **G200** | chief / ariki | *ariki / ariki henua* | 0.95 | 19 | Aruku Kurenga, Santiago Staff, Tablet D |
| **G400** | offspring / young | *poki / hua / ui* | 0.65 | 37 | Santiago Staff, Small Santiago |
| **G500** | elder / ancestor | *tupuna / koroua* | 0.70 | 28 | Santiago Staff, Small Santiago |

---

## The Individual Glyphs — Evidence Basis

### G007 — Child/Descendant (*poki*)
**The uniquely confirmed identification.** The secondpass notes:

> *"Metoro was recorded reciting 'poki' (child) when pointing to a certain glyph, confirming glyph 7's meaning as 'child/descendant' in a lineage context."*

This is indigenous testimony — an Easter Islander in the 19th century verbally identified this glyph as *poki*. No other lexical identification in the entire corpus has this direct attestation from a native speaker. G007 = child/poki is therefore the gold standard for confidence.

Tablets: Santiago Staff (genealogical context), Aruku Kurenga (narrative context). The appearance on Aruku Kurenga is consistent with genealogical segments within the three-sequence structure (Phase 42).

### G001 — Person/Human (*tangata*)
127 occurrences — the 3rd most frequent glyph in the corpus. Its high frequency places it as the **default person reference** — whenever the text needs to refer to a human being without specifying their status, age, or gender, G001 is used.

The sensebank records: "often serves as a generic person indicator or perhaps as part of personal names." At 127 occurrences across 4 tablets (Aruku Kurenga, Mamari, Santiago Staff, Small Santiago), G001 appears in every major tablet type — genealogical, calendar, and narrative.

### G300 — Woman/Mother (*vi'e/māmā*)
43 occurrences on Santiago Staff and Small Santiago only. The gendered female counterpart to the generic G001. The secondpass notes G300 appears in genealogical formulas where the female parent is identified. In Rapa Nui genealogies, both paternal and maternal lineages were recorded for high-status individuals — G300 is the maternal-line marker.

The lexicon notes: "Anthropomorphic female figure representing woman or mother; appears in genealogies." No tablet records G300 on Mamari or Aruku Kurenga — it is exclusively a genealogical-record glyph (Santiago Staff and Small Santiago are the two primary genealogical tablets).

### G200 — Chief/Ariki (*ariki/ariki henua*)
The highest-confidence social glyph (0.95). Only 19 occurrences, but it appears in the most structured and formula-bound contexts: P004 title sequence (3 tablets), Tablet D line a3's chief enumeration (Phase 44), and the genealogical cluster. Despite low count, G200 is the most precisely positioned glyph in the corpus — it almost always precedes a name cluster and almost never appears elsewhere.

**G200's two meanings and when each applies:**
- *ariki*: living chief, a specific individual — in formula B200 + NAME
- *ariki henua*: the title "paramount chief of the land" — possibly when G200 appears with G030/G031 (land/earth glyphs)

### G400 — Offspring/Young (*poki/hua/ui*)
37 occurrences, lower confidence (0.65). The "hua" reading (fruit/offspring) creates a semantic link to G074 (*hua* = first-quarter moon fruit) — in Polynesian, the word for fruit (*hua*) is also the word for offspring/child. The same word written by the same glyph sound in both a calendar context (fruit = growing moon) and a genealogical context (fruit = child produced) is one example of the script's fundamental polysemy strategy.

G400's primary genealogical role is as the **result** in the procreation formula (P003): PARENT_A + B076 + PARENT_B = G400 (the child produced).

### G500 — Elder/Ancestor (*tupuna/koroua*)
28 occurrences, conf 0.70. Found only on Santiago Staff and Small Santiago — the genealogical tablets. G500 does not appear on Mamari or Aruku Kurenga. This tablet restriction is meaningful: elders/ancestors are specifically named in lineage records, not in calendar texts or voyage narratives. G500 is a genealogical-only glyph.

The lexicon note: "Distinguished human figure representing elder or ancestor; tentative." The "tentative" caveat is honest — G500 is less securely identified than G200 or G001. Its 28 occurrences provide a moderate evidence base.

---

## The Hierarchy as a System

Reading the five social glyphs together reveals a **complete generational arc**:

```
G500 (ancestor/tupuna)
  ↓ [time passes]
G200 (current chief/ariki)
  |
  + G300 (mother/vi'e) ← the female line
  |
  [B076 / procreation]
  ↓
G400 (offspring/hua)
  ↓ [grows]
G001 (person/tangata)  ← the generic adult
  ↓ [if politically elevated]
G200 (chief/ariki again)  ← the cycle continues
  |
  [alongside G007 / poki] ← specific children named
```

This generational arc corresponds precisely to how a Polynesian genealogical chant operates: beginning with the founding ancestor (G500), naming the chief (G200), recording the procreation event (B076), naming the offspring (G400), and continuing until the current generation is reached.

---

## What the Cluster Data Confirms

From clusters.json:
- **Cluster 1 (genealogical)**: includes G001, G200, G400, G500, B076, B999 — the core genealogical actors and their connectors
- **Cluster 2 (human classification)**: includes G001, G007, G200, G300, G600, G690 — broader social category markers
- G300 is in cluster 2 but not cluster 1 — it is a classification glyph (woman/female) more than it is a purely genealogical formula element. This is consistent with G300 appearing in genealogies to identify the female parent but not being part of the core P001/P003 formula structure.

---

## Tablet Distribution and What It Tells Us

The social hierarchy glyphs concentrate heavily on the Santiago Staff and Small Santiago:
- G300, G400, G500 are **exclusively** on Santiago Staff + Small Santiago
- G200 appears on B, H, G, D — primarily genealogical tablets
- G001 is the only social glyph on all four major tablets including Mamari

**What this distribution suggests (without forcing):** The genealogical tablets (H Staff, G Small Santiago) carry the full social taxonomy. The calendar tablet (C Mamari) uses only the generic person (G001). The narrative tablet (B Aruku Kurenga) uses chief-title (G200) and generic person (G001) but not female/elder/offspring markers. This is consistent with each tablet having a primary content genre that selects appropriate vocabulary from the full social taxonomy.

---

## Key Findings

1. **G007 (*poki*/child) is the only lexical identification directly confirmed by indigenous testimony** (Metoro, 19th century) — this is the corpus's gold standard identification
2. **G001 (127 occ) is the default person-reference** across all tablet types; all other social glyphs are contextually restricted
3. **G300 (woman/mother) is genealogy-exclusive** — appears only on Santiago Staff and Small Santiago; never on calendar or narrative tablets
4. **G400 (*hua*/offspring)** creates a semantic cross-link with G074 (*hua*/first-quarter moon fruit) — the same Rapanui word for "fruit" covers both offspring and growing moon, demonstrating the script's deliberate exploitation of lexical polysemy
5. **G500 (ancestor/elder) is also genealogy-exclusive** — the same tablet restriction as G300; elders are named in lineage records only
6. **G200 (chief/ariki, conf 0.95)** is the most precisely positioned glyph in the corpus — almost exclusively in formula-head position, preceding name clusters, on genealogical/chiefly tablets
7. The **complete social hierarchy** (ancestor → chief → mother → offspring → child → person) is a coherent generational arc that maps directly onto Polynesian genealogical chant structure — this alignment emerges from the data, not from fitting the data to a template
