# Phase 1 — Corpus Assembly & Provenance Hardening

**Date:** 2025-10-28  
**Status:** Complete (Updated with 2025-09-26 MASTER lexicon)  
**Goal:** Assemble a lossless, attested corpus with locked provenance

## Data Sources

### Primary Lexicons
1. **MASTER Lexicon (Updated)**: `rongorongo_lexicon_MASTER_2025-09-26.updated.json`
   - **734 lexicon entries** (expanded from 306)
   - **629 total glyphs documented**
   - Barthel numeric IDs (1..999) + project composites
   - Full attribution to Lackadaisical Security (Operator) and Spectre

2. **Enhanced Multi-Meaning Lexicon**: `Enhanced_Multi_Meaning_Rongorongo_Lexicon.json`
   - 47 enhanced entries with polysemic interpretations
   - Version 5.0 (August 5, 2025)
   - 32 polysemic glyphs identified

3. **Complete Lexicon**: `final_complete_rongorongo_lexicon.json`
   - 306 glyph entries
   - Comprehensive cross-referenced translations

### Research Archive
- **rongorongo-research.zip**: 1.8 MB archive containing:
  - 53 detailed markdown research files (rongorongo1.md through rongorongo53.md)
  - Multiple lexicon versions (JSON, CSV, JSV formats)
  - Comprehensive analysis documents
  - License and attribution files

### Second Pass Phase Documents
- **15 detailed PDF phase documents** covering Phase 1-15 of second pass analysis
- **Main overview document**: rongorongo-secondpass.pdf
- Full decipherment methodology and results

## Corpus Structure

All data has been normalized into the repository structure:

```
/corpus/normalized/     # Normalized glyph data from lexicons
/corpus/variants/       # Variant and ligature mappings
/corpus/parallels/      # Cross-tablet alignments
```

## Provenance Tracking

Every glyph entry includes:
- **Source attribution**: Primary researchers (Barthel, Fischer, Pozdniakov, etc.)
- **Confidence scores**: 0.0 - 1.0 scale
- **Context types**: genealogical, astronomical, marine, etc.
- **Occurrence data**: Tablet locations and frequencies
- **Tablets found**: Specific tablets where glyph appears

## Quality Assurance

✓ **Coverage**: 734 glyphs with multi-sense modeling (expanded from 306)  
✓ **Provenance**: All sources tracked and attributed  
✓ **Format**: Lossless JSON preservation of all variant meanings  
✓ **Hashing**: Run metadata includes checksums and timestamps  
✓ **Documentation**: Second pass phase PDFs integrated

## Outputs

- `banks/sensebank.json` - 734 glyphs with 558 sense entries
- `banks/namebank.json` - 33 name candidates (expanded from 14)
- `banks/calendarbank.json` - 32 calendar entries (expanded from 14)
- `banks/numeralbank.json` - 8 numeral candidates (expanded from 2)
- Run tracking: `runs/20251028_222914/run.json`

## Update Summary (2025-09-26)

**Improvements:**
- Expanded from 306 to 734 glyph entries (+428 glyphs, +140% increase)
- Increased name candidates from 14 to 33 (+136%)
- Expanded calendar entries from 14 to 32 (+129%)
- Increased numeral candidates from 2 to 8 (+300%)
- Total sense entries: 558 (previously 138)

## Next Steps

Phase 2 will establish variant and ligature discipline, ensuring no silent collapses of glyph variants.
