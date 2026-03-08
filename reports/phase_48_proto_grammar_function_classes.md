# Phase 48 — Proto-Grammar: What the Structural Data Actually Shows

**Date:** 2026-03-08  
**Status:** Complete — proto_grammar.json and secondpass data-grounded  
**Sources:** proto_grammar.json; segmentation_v2.json; constraints.json; secondpass-phase5-5.4.md; secondpass-phase14.md

---

## Framing: What "Proto-Grammar" Means Here

Rongorongo is documented in proto_grammar.json as:

```
script_nature:
  type: "Proto-writing / Mnemonic device"
  characteristics:
    - "Logographic (not fully phonetic)"
    - "Elliptical style (omits grammatical particles)"
    - "Context-dependent interpretation"
    - "Encodes key concept-words for oral expansion"
  implication: "Grammar is partially implicit, inferred by knowledgeable reader"
```

This framing is essential for all grammatical analysis. The script encodes **key concept-words** — the high-information nodes — and omits the connective tissue (particles, articles, case-markers) that a chanter would supply from memory. Analysing Rongorongo's grammar means identifying what *is* written (the content nodes and the explicit relational operators) rather than reconstructing what is implied.

---

## Function Class 1: Relational Operators (most secure)

The most firmly established functional class, based on convergent evidence from parallel passages and cluster data:

**B076** (*'ai/fanau* — beget/copulate): Appears as the central element of the genealogical formula on 4 tablets (P001, P003). Its function is to **link two noun-glyphs in a generative relationship**. This is the closest thing to an identified verb in the corpus.
- Evidence level: HIGH — 15 confirmed occurrences, cross-tablet, 0.92 alignment

**B062** (clause break, *ki*): Listed in the lexicon as "clause break" with conf 0.80 and 67 occurrences. Listed in the parallel passages data as a "temporal marker." Its high frequency (67 occ) without a strong lexical content meaning suggests it is primarily structural — a marker that separates one clause from the next.
- Evidence level: MODERATE — frequency and position consistent with a clause-boundary role

**B999** (section divider): Confirmed from Santiago Staff data — 103 occurrences, pure punctuation marker, "not vocalized." Appears in the genealogical cluster.
- Evidence level: HIGH — explicitly confirmed, no lexical meaning claimed

---

## Function Class 2: Social Hierarchy / Title Markers

The proto_grammar.json explicitly lists these as a functional class:

**B200** (*ariki/chief*, conf 0.95): Title marker preceding personal names. Confirmed in P004 (title sequence) on 3 tablets.

**B001** (*tangata/person*, conf 0.85): Generic person marker. The "default" human indicator — the baseline on which B200 (elevated person) and B400/B007 (juvenile persons) are variations.

**B007** (*poki/child/descendant*, conf 0.80): Descendant marker. Explicitly confirmed by a 19th-century native reading: Metoro was recorded saying "poki" (child) when pointing to a specific glyph, confirming this identification from indigenous testimony.

**B300** (*vi'e/māmā* — woman/mother, conf 0.75): Female person marker. The gendered counterpart to B001's generic person.

**B400** (*poki/ui* — offspring/young, conf 0.65): Offspring marker; appears as the product of the procreation formula (P003).

**B500** (*tupuna/koroua* — ancestor/elder, conf 0.70): Elder marker — the oldest generation tier.

---

## Function Class 3: Plural / Quantitative Markers

**B006** (*rima/ma'u* — hand/plural, conf 0.90, 156 occ): The highest-frequency glyph in the corpus. Its function as a plural marker is documented in proto_grammar.json and confirmed by the Tablet D analysis (Phase 44) where the secondpass explicitly states "glyph 6 ('hand') is understood as a plural marker when attached to another glyph — an insight gained by observing it consistently suffixed to nouns to indicate plural or collective forms in various texts."

The hand-as-plural logic: *rima* = hand = five (fingers) = many/group. The same conceptual bridge exists in other Polynesian languages. This is not imposed — it is a transparent semantic derivation.

At 156 occurrences (5.62% of the corpus), B006 is the **most frequent glyph in all of Rongorongo**. If it functions primarily as a plural marker, then roughly 1 in 18 glyphs in the entire corpus is a grammatical plurality marker. This is an extremely high grammatical density — it suggests the texts frequently reference multiple persons, objects, or actions simultaneously rather than listing singular items.

---

## Function Class 4: Structural Delimiters

**B032** (*mata/section delimiter*, conf 0.80, 89 occ): Section start marker. Confirmed on Aruku Kurenga (Phase 42) and Santiago Staff. 89 occurrences make it the 7th most frequent glyph — grammatically significant.

**B062** (clause break, 67 occ): As above.

**B999** (section divider, 103 occ on Santiago Staff): As above.

Together these three structural glyphs account for 259 occurrences — roughly **9.3% of the entire corpus** is structural punctuation. This is a high proportion and means Rongorongo texts are heavily segmented — the scribes organised their content into discrete bounded units, not continuous flow.

---

## Word Order — What the Data Suggests

Proto_grammar.json records word order patterns inferred from grammatical pattern analysis:

The genealogical formula pattern is:
```
[TITLE] + [NAME] + [RELATOR] + [NAME/OUTCOME]
B200   + NAME   + B076       + NAME/B400
```

This is **title/agent → relation → patient/result** — consistent with a head-initial ordering where the title precedes the name, the agent precedes the action, and the result follows the action. 

In Rapa Nui as a spoken language, VSO (verb-subject-object) order is attested. But the genealogical formula appears to follow SOV or SVO with the relator/verb as medial element. This is not necessarily a contradiction — the written formula may be elliptical, omitting particles that would establish the spoken word order.

**What we can say without forcing:** The genealogical formula has a consistent three-part structure with the relator always in the middle position. Whether this is SOV, SVO, or something else depends on how B076 and B200 are classified — a question that requires more data.

---

## Phonotactic Constraints — What the Lexicon Suggests

From constraints.json:
```
phonotactic_rules:
  cv_bias: Rapanui strongly favours CV (consonant-vowel) syllable structure
  vowel_endings: All Rapanui words end in vowels
  no_consonant_clusters: No clusters of consonants permitted
```

These constraints, if the script encodes Rapanui phonology, mean:
- Transliterations that end in consonants (unlikely in Rapanui) may be non-Rapanui borrowings or scribal conventions
- The short transliterations in the lexicon (*ika*, *manu*, *rima*, *mata*, *poki*) all conform to CV patterns — consistent with genuine Rapanui forms
- Longer proposed transliterations with consonant clusters should be treated with lower confidence

---

## What This Phase Establishes

1. **B076 is the most secure verb-equivalent** in the corpus — confirmed by 15 cross-tablet occurrences in the genealogical/procreation formula as a relational operator
2. **B006 (hand/plural)** is the most frequent glyph overall — at 5.62% of the corpus, its grammatical plurality function means roughly 1 in 18 glyphs is a pluraliser
3. **~9.3% of the corpus is structural punctuation** (B032, B062, B999 combined) — the texts are heavily segmented into discrete bounded units
4. **The genealogical formula has a fixed three-part structure** (title/agent + B076 + name/result) consistent with but not proving any specific Polynesian word order
5. **B007's identification as "child/poki"** is the only lexical identification directly confirmed by 19th-century indigenous testimony (Metoro)
6. The script's **elliptical style** (omitting particles, articles, case-markers) means grammar is partially implicit — the proto-grammar analysis reveals the explicit structural skeleton, not the full implied sentence

---

*"We can see the bones of the sentence — the chief, the begetting, the offspring, the divider. The flesh — the particles, the pronouns, the tense markers — was supplied by the chanter from memory. We have the score; we're missing the musician."*
