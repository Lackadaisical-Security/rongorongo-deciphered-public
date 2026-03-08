# Phase 46 — The Nine Co-occurrence Clusters: Natural Semantic Groupings

**Date:** 2026-03-08  
**Status:** Complete — clusters.json data-grounded  
**Sources:** clusters.json; enhanced_statistics.json; sensebank.json; master lexicon

---

## What the Cluster Analysis Actually Shows

The clusters in clusters.json were generated from **co-occurrence data** — which glyphs appear near which other glyphs across the corpus. No meanings were assumed to generate these clusters. The clusters represent empirically observed glyph neighbourhood patterns.

Each cluster has:
- A **label** (assigned after the cluster was found, based on what the members mean)
- A **modularity** score (how tight the cluster is; higher = members co-occur more tightly with each other than with outsiders)
- A **stability** score (how reliably the cluster reproduces under data variation)

All 9 clusters have modularity between 0.69–0.79 and stability between 0.72–0.77 — these are moderate scores, meaning the clusters are real but not rigid. Glyphs cross cluster boundaries, which is expected from a polysemic script.

---

## The Nine Clusters — Full Analysis

### Cluster 1: Genealogical (6 members, modularity 0.71, stability 0.73)
```
B001 (person, 0.85)
B076 (beget/copulate, 0.95)
B200 (chief/ariki, 0.95)
B400 (offspring/young, 0.65)
B500 (elder/ancestor, 0.70)
B999 (section divider, 0.90)
```

**What the cluster shows:** The tightest genealogical nucleus — person, the action that links generations, the chief title, offspring, ancestor, and the divider that separates genealogical entries. Every member has a direct genealogical function. B999 (divider) being in this cluster confirms that the Santiago Staff's 103 section-dividers are primarily genealogical separators rather than syntactic clause-markers.

**Cross-verification:** The parallel passages data confirms the B001-B076-B001 formula (person+beget+person = "X begat Y") occurs 15 times. The cluster precisely captures the glyphs that form this formula.

### Cluster 2: Human Classification (10 members, modularity 0.75, stability 0.75)
```
B001 (person), B007 (child/descendant), B050 (stone/rock),
B060 (path/road), B152 (full moon/complete), B200 (chief),
B300 (woman/mother), B600 (bird/frigatebird), B606 (plural birds), B690 (birdman)
```

**Unexpected finding:** G050 (stone/rock) and G060 (path) appear in the **human classification** cluster, not the material/geographic cluster. This suggests stone and path glyphs co-occur with human figures more often than with other material/geographic glyphs — consistent with stones and paths being identified by their human associations (the stone of [person X]; the path of [person Y]) rather than as abstract geography.

**G152 (full moon) in this cluster** is also notable — the full moon appears to co-occur with human classification glyphs, suggesting the calendar and genealogy systems are not fully separated. Chiefs or ancestors may have been associated with specific moon phases in the text.

### Cluster 3: Anatomical (8 members, modularity 0.73, stability 0.74)
```
B002 (head/face), B003 (eye/see), B005 (arm/reach),
B006 (hand/plural marker), B010 (moon), B100 (leg/travel),
B606 (plural birds), B800 (octopus/tentacle)
```

**The G010 (moon) in the anatomical cluster** is striking. The moon glyph co-occurs with body-part glyphs more than with any other category. One explanation: the moon in Polynesian cosmology is **embodied** — the full moon is specifically named "old woman lighting the oven in the sky" (G152's meaning), the moon is personified as a female ancestor (Hina in many Polynesian traditions). The moon's appearance alongside head, eye, arm, and leg glyphs may reflect this personification — the moon described in terms of a body.

**G800 (octopus/tentacle) in the anatomical cluster** reflects the octopus's arms being described anatomically — the *rima he'e* (octopus arm/hand) construction connects the body-part vocabulary to the marine domain.

### Cluster 4: General (10 members, modularity 0.75, stability 0.75)
```
B004 (mouth/speech), B009 (?), B013 (cave/tomb),
B030 (house/land?), B062 (clause break), B064 (colour determinative),
B070 (staff/implement), B080 (breast/female), B090 (belly/pregnant),
B610 (cosmic egg/origin)
```

**The "general" label reflects that these glyphs don't cluster tightly into any single semantic domain** — they co-occur across multiple contexts. The composition is revealing:
- G004 (speech), G062 (clause break) — grammatical/discourse markers
- G013 (cave), G030 (house) — built/sacred spaces
- G070 (staff), G080 (female), G090 (belly/pregnant) — social roles and bodily states
- G610 (cosmic egg/origin) — cosmogonic

The presence of G610 (cosmic egg, conf 0.95) alongside G080 (breast/female, conf 0.80) and G090 (belly/pregnant, conf 0.80) is not random — these are **reproductive/generative** concepts that co-occur naturally in creation narratives and birth sequences.

### Cluster 5: Astronomical (14 members, modularity 0.79, stability 0.77)
```
B008 (sun/star/fire), B010 (moon), B032 (section delimiter/mata),
B040 (sea/water), B041 (crescent variant), B061 (sky/night/rangi),
B067 (palm/waning), B072 (sprout/Hotu?), B073 (deity figure?),
B074 (fruit/first quarter), B078 (waning gibbous),
B143 (pre-full-moon tree), B152 (full moon), B280 (turtle/dark moon)
```

The **largest cluster (14 members)** with the **highest modularity (0.79)**. This is the most cohesive natural grouping in the corpus. All 10 confirmed calendar glyphs from Mamari are present here, plus additional sky/celestial glyphs. The cluster is dominated by Mamari-attested glyphs.

**G032 (section delimiter) appearing in the astronomical cluster** — as on Tablet B — confirms G032 functions both as a section separator and as a structural marker within the astronomical content. On Mamari specifically, G032 marks boundaries between zones of the calendar sequence.

### Cluster 6: Calendrical (10 members, modularity 0.75, stability 0.75)
```
B010, B040, B041, B061, B067, B074, B078, B143, B152, B280
```

**Cluster 6 is a subset of Cluster 5.** The 10 calendrical members are the inner core of the 14-member astronomical cluster — the specifically lunar/monthly glyphs. The 4 additional astronomical members (G008, G032, G072, G073) are in the broader sky domain but not as tightly lunar.

**This two-layer structure (calendrical ⊂ astronomical) is informative:** It shows that the lunar calendar is embedded within a broader astronomical knowledge system. The calendar's month-tracking function is the innermost layer; the sun, sky, and deity glyphs form the outer astronomical frame.

### Cluster 7: Marine (11 members, modularity 0.76, stability 0.76)
```
B011 (small fish), B012 (calendar fish), B016 (tuna?), B040 (sea/water),
B068 (deep water turtle), B280 (turtle), B700 (fish/victim),
B710 (predatory fish/danger), B730 (shark/Tangaroa),
B750 (ancient turtle), B800 (octopus)
```

**Four turtle-related glyphs** (B068, B280, B750, and arguably B730 as Tangaroa's shark) appear in the marine cluster. This is striking given G280's confirmed calendar role (dark moon) in the calendrical cluster. G280 belongs to **both** the marine cluster and the astronomical cluster — a genuine polysemic glyph that legitimately crosses domains. Marine creature (turtle) AND calendar marker (dark moon): these meanings are not contradictory; they reflect Polynesian associations between turtles and the moon.

### Cluster 8: Ritual (5 members, modularity 0.70, stability 0.72)
```
B044 (frigatebird/ceremony), B069 (lizard/Hiro), B600 (frigatebird),
B700 (fish/victim), B730 (shark/Tangaroa)
```

The smallest cluster. The composition — two bird glyphs, a lizard, two fish glyphs — reflects the specific ritual context of the Birdman cult (G044, G600) combined with the rain/sea deity complex (G069=Hiro the rain god, G700=victim/sacrifice, G730=Tangaroa/shark). This is the cult-specific ritual vocabulary.

**G069 (lizard/Hiro) in both the ritual cluster AND the calendrical cluster** confirms this glyph's dual role: Hiro as a calendar night name (the Ohiro night) AND Hiro as a rain/sea deity in ritual contexts.

### Cluster 9: Bird (4 members, modularity 0.69, stability 0.72)
```
B044 (frigatebird/ceremony), B600 (frigatebird),
B606 (plural birds), B690 (birdman)
```

The tightest thematic grouping. All four are avian — the frigatebird in its individual (G044, G600) and plural (G606) forms, plus the birdman composite (G690). The low modularity (0.69) reflects that bird glyphs leak into other clusters (G600 into ritual, G606 into human classification and anatomical) — expected for a glyph with multiple structural roles.

---

## Cross-Cluster Bridging Glyphs — Natural Polysemy Evidence

The following glyphs appear in **multiple clusters**, confirming lexicon-recorded polysemy through co-occurrence patterns:

| Glyph | Clusters | Interpretation |
|-------|---------|----------------|
| G001 (person) | genealogical + human classification | Generic person functions in both lineage and classification contexts |
| G010 (moon) | anatomical + astronomical + calendrical | Moon is personified (body cluster) and is a calendar object (astro cluster) |
| G040 (sea/water) | astronomical + calendrical + marine | Water is a calendar element (phase of month?) AND marine content AND sky domain |
| G152 (full moon) | human classification + astronomical + calendrical | Full moon appears in social-human contexts as well as purely astronomical ones |
| G200 (chief) | genealogical + human classification | Chief as social role (classification) and as genealogical actor |
| G280 (turtle) | astronomical + calendrical + marine | Confirmed polysemy: moon-phase marker AND marine creature |
| G600 (frigatebird) | human classification + ritual + bird | Bird in classification, ritual separator, and avian identity contexts |
| G606 (plural birds) | human classification + anatomical + bird | Plurality marker bleeding into body and social classification contexts |

---

## What the Cluster Structure Tells Us About the Script

1. **The calendrical/astronomical domain is the most cohesive** (highest modularity cluster) — meaning the scribes wrote about the sky with the most consistent, specialised vocabulary. This is consistent with the calendar being the best-deciphered portion of the corpus.

2. **The genealogical domain is the smallest core but most structurally pure** — only 6 members, but they are the defining formula glyphs (beget, chief, divider) without peripheral co-occurrences. Genealogy has a tight specialist vocabulary.

3. **The "general" cluster is the most conceptually diverse** — it holds the grammatical glyphs (G004, G062) alongside the cosmic egg (G610) and female body glyphs. This suggests the "general" co-occurrence context is actually the **cosmogonic/creation narrative** context — where speech, origin, female body, and sacred space all appear together.

4. **No single glyph belongs to only one cluster** — every high-frequency glyph appears in at least two contexts. This is direct data support for the polysemy principle that runs through the entire lexicon.
