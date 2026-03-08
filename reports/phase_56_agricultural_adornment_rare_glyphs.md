# Phase 56 — The Agricultural and Adornment Vocabulary: Rare Glyphs in Context

**Date:** 2026-03-08  
**Status:** Complete — sensebank and lexicon data-grounded  
**Note on low-occurrence glyphs:** This phase covers glyphs with occurrence_count of 1–3 in the current data. Low occurrence means high uncertainty — these identifications are provisional and should be treated as lower confidence than the corpus's high-frequency anchors.

---

## The Rare-Glyph Problem

Of 309 documented unique glyph types, 251 appear only once (Phase 51). This phase addresses a specific subset: **agricultural, craft, and adornment glyphs** that appear rarely but whose iconographic forms are reasonably interpretable.

The cross-validation data (Phase cross_validation.json) found:
- **Multi-source agreement: 10.49%** — only 10.49% of 77 glyphs checked had multiple sources agreeing on meaning. This is the validation system's way of flagging that rare-glyph identifications are overwhelmingly single-source.
- **Context consistency: WARNING** — 0 cross-verified contexts out of 111

This means the rare agricultural/adornment glyphs must be treated as **tentative visual identifications**, not confirmed readings.

---

## Agricultural Glyphs (All with occ=1, no tablet attestation)

### G018 — Fruit/Yield (*hua*, conf 0.75)
Transliteration *hua* = fruit or yield. The same root word as G074 (*Hua*/first-quarter moon) and G400 (*hua*/offspring). The agricultural *hua* (crop fruit) is one of three *hua* meanings distributed across three different glyphs — demonstrating how the script consistently exploits lexical polysemy but uses distinct glyph forms to differentiate contexts.

**The absence of a tablet attestation** (empty tablets_found list) raises a serious flag: if G018 has 0 confirmed tablet appearances, its identification is based entirely on iconographic inference from its form, not from contextual analysis of its actual position in a text. This is the weakest evidentiary basis for any identification.

### G019 — Yam/Tuber (*ufi*, conf 0.75)
The yam (*ufi*) was the primary agricultural staple of Polynesian societies. Easter Island had limited agricultural diversity; yams and sweet potato (*kumara*) were the most important crops. A yam glyph would appear in agricultural lists, tribute records, or seasonal planting instructions. Again, no tablet attestation listed — iconographic identification only.

### G021 — Banana/Plantain (*meika*, conf 0.75)
The banana (*meika*) was cultivated on Easter Island though not as abundantly as on larger Polynesian islands. Its curved form makes for a visually distinctive glyph if represented iconographically. No tablet attestation.

**The agricultural triad (G018 fruit, G019 yam, G021 banana) has a common problem:** All three have 0 confirmed tablet occurrences in the current data. Their identifications rest on visual analogy (the glyph looks like the thing it names) rather than contextual or statistical evidence. These identifications are **plausible but unverified**.

---

## Fire and Cooking: G033 (*ahi*, conf 0.75)

*Ahi* = fire. The fire glyph in a Polynesian context encodes not just the physical element but the entire cultural complex of fire: the *umu* (earth oven), the ceremonial fire for *hi'u* purification rituals, the cooking fire that transforms raw food. In the corpus data, G033's second sense is "chief/royal title" — fire as a metaphor for chiefly power (the chief who lights the sacred fire, the fire that cannot be extinguished).

No tablet attestation listed. However, G033 (*ahi*/fire) appearing in the **general cluster** (cluster_4) alongside G090 (belly/pregnant, conf 0.80) and G610 (cosmic egg) is consistent with fire in creation contexts — the cosmic fire at the beginning of the world, or the fire of life kindled at birth.

---

## Adornment Glyphs

### G027 — Tattoo (*tatū*, conf 0.75)
*Tatū* = tattoo. The word *tattoo* itself is borrowed from Polynesian into English (from Tahitian *tātau*). Easter Island tattoo culture was documented by early European visitors as highly elaborate — chiefs and warriors had complex full-body tattoos (*tatū*) that encoded status, genealogy, and ritual protection. A tattoo glyph in a chiefly genealogical text would mark specific individuals known for their tattooing, or record the tattoo patterns of clan groups.

No tablet attestation. Single source identification.

### G038 — Feather (*hulu*, conf 0.75)
*Hulu* = feather, adornment. Feathers (*hulu*) were used in the headdresses (*hami*) of warriors and chiefs. The Birdman competition winner wore a specific feathered headpiece. Feather-work ornaments were traded items and status markers across Polynesia. A feather glyph in a chiefly text might mark a chief renowned for their feather ornaments, or appear in a tribute list alongside other prestige objects.

No tablet attestation.

### G026 — Ornament/Rei Pendant (*rei*, conf 0.75)
*Rei* = a pendant or ornament, specifically the *rei miro* (whale-tooth or whale-ivory crescent pendant) worn by high-status Rapanui. The *rei miro* was one of the most distinctive Rapa Nui prestige objects — elongated, curved, worn at the chest. If G026 depicts the *rei miro*, it marks the wearer as high status. Appearances alongside G200 (chief) would be particularly diagnostic.

No tablet attestation.

---

## G035/G036 — Venus as Morning and Evening Star

### G035 — Morning Star / Hine (*hetu pu/Hine*, conf 0.75)
- *Hine* = Venus as morning star (goddess name)
- *hetu pu* = star of dawn

### G036 — Evening Star (*hetu ahiahi*, conf 0.75)
- *hetu ahiahi* = evening star (Venus in its evening manifestation)

Both have occurrence_count=1 with no tablet attestation listed.

**The Venus identification** is important despite the low attestation because:
1. Venus is the brightest star/planet visible to the naked eye — it would be the most prominently tracked celestial object after the sun and moon
2. In many Polynesian traditions, Venus (morning star) is the navigator's guide for east-west travel — critical for open-ocean voyaging
3. Hine as Venus-goddess connects to the Rapa Nui female deity tradition (Hina/Hine as the moon woman)

**However:** Without confirmed tablet attestation, G035 and G036 cannot be confidently placed in the calendrical system. Their identification is iconographic/culturally derived, not corpus-statistical.

---

## G061 — Sky/Night/Rangi (*rangi/po/hetu'u*, conf 0.70)

**56 occurrences** — rank 19 in the top-20. This is not a rare glyph; it belongs to the high-frequency set but hasn't been discussed deeply yet.

G061 encodes three distinct but related concepts:
- *rangi*: sky (the physical dome)
- *po*: night (the sky at night = the nighttime sky = the domain of stars and moon)
- *hetu'u*: star

The triple reading is coherent — night/sky/star are inseparable aspects of the same celestial dome as observed from Rapa Nui's position in the Pacific, under one of the clearest night skies on Earth.

**G061 on Mamari and Santiago Staff:** Its appearance on the calendar tablet (Mamari) is expected — sky/night is the backdrop for all lunar calendar observations. Its appearance on the Santiago Staff may encode specific star associations for particular chiefs (being born under a specific star, or being named after a star phenomenon).

G061's membership in both the **astronomical cluster** and the **calendrical cluster** confirms it bridges sky-observation and time-reckoning — the night sky is both the subject of observation and the instrument of timekeeping.

---

## G610 — Cosmic Egg/Origin (*hua/mata/mata-source*, conf 0.95)

**22 occurrences**, Santiago Staff and Small Santiago. The highest-confidence cosmogonic identification.

G610 (*hua* = egg = origin; *mata* = source/beginning) is the **cosmic egg** — the primordial egg from which creation emerges, a concept found in Polynesian creation myths. In Māori tradition, *Ranginui* (sky father) and *Papatūānuku* (earth mother) are sometimes said to have been enclosed in a cosmic egg before the world's creation.

G610 in the "general" cluster alongside G080 (breast/birth) and G090 (belly/pregnant) is the cosmogonic birth complex — egg → womb → birth = the three stages of cosmic creation from nothingness to form.

**G610's tablet restriction to Santiago Staff and Small Santiago** means cosmic origin narratives appear specifically in the genealogical texts — the beginning of a lineage is framed as a cosmic creation event. The founding ancestor's birth = the beginning of the world.

---

## Key Findings

1. **The agricultural glyphs (G018, G019, G021) have zero confirmed tablet attestation** — their identifications are iconographic/provisional, and this must be stated clearly; they should not be used as evidence in cross-tablet analyses
2. **The adornment glyphs (G027 tattoo, G038 feather, G026 rei-ornament)** are similarly unattested in the current data — plausible from cultural context but not corpus-confirmed
3. **G035/G036 (Venus morning/evening)** are important cultural identifications but lack tablet attestation — the Venus identification is culturally reasonable but remains in the "iconographic inference" category
4. **G061 (sky/night/rangi, rank 19, 56 occ)** is a high-frequency glyph that bridges astronomical and calendrical clusters — the nighttime sky as simultaneously the object of calendar observation and the domain of star-navigation
5. **G610 (cosmic egg/origin, conf 0.95, 22 occ)** is restricted to genealogical tablets — founding-ancestor birth = cosmic creation event in the script's logic
6. The **cross-validation warning** (multi-source agreement 10.49%, context consistency WARNING) applies most strongly to the rare/unattested glyphs discussed here — the quality assessment demands honest calibration: rare glyphs should be treated as provisional even when they carry visually compelling identifications
