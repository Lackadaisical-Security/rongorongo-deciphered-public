# Rongorongo Tablet Photographs

**Last Updated:** November 9, 2025
**Total Images:** 19 photographs
**Total Tablets:** 12 tablets
**Total Size:** ~5.1 MB
**Location:** `inputs/images/`

## Overview

This directory contains high-resolution photographs of authentic Rongorongo tablets for visual analysis, topology verification, and sequence extraction. These images support Phases 1 (Corpus Assembly), 3 (Orientation & Line Topology), and ongoing visual verification tasks.

## Tablet Inventory

### Tablet B — Aruku Kurenga (Great Tradition)

**File:** `tablet_B_recto.jpg` (512 KB)
**Description:** One of the longest known tablets, contains extensive genealogical sequences
**Referenced in Phase 3:** 50 lines documented
**Key Features:** Boustrophedon reading pattern, genealogical formulas
**Current Analysis:** High-confidence for genealogical studies

---

### Tablet C — Mamari (Lunar Calendar Tablet)

**Files:**
- `tablet_C_recto.jpg` (535 KB)
- `tablet_C_verso.jpg` (810 KB)

**Description:** Famous for its lunar calendar sequences
**Referenced in Phase 3:** 29 lines documented
**Referenced in Phase 12:** Primary source for calendar analysis
**Key Features:**
- Lunar cycle patterns (29-30 day sequences)
- B152-series glyphs (lunar phases)
- Moon phase progression markers

**Current Analysis:** Critical for calendrical studies, 98% alignment score for lunar pattern P002

---

### Tablet D — Échancrée

**Files:**
- `tablet_D_sideA.jpg` (472 KB)
- `tablet_D_sideB.jpg` (473 KB)

**Description:** Medium-sized tablet with both sides preserved
**Key Features:** Clear glyph preservation, moderate damage
**Current Analysis:** Available for sequence analysis

---

### Tablet E — Keiti

**Files:**
- `tablet_E_recto.jpg` (264 KB)
- `tablet_E_verso.jpg` (278 KB)

**Description:** Well-preserved tablet with both surfaces
**Key Features:** High-resolution details, minimal wear
**Current Analysis:** Suitable for variant glyph identification

---

### Tablet F — Chauvet Fragment

**Files:**
- `tablet_F_sideA.jpg` (170 KB)
- `tablet_F_sideB.jpg` (30 KB)

**Description:** Fragmentary tablet, incomplete but valuable
**Key Features:** Side B heavily damaged (small file size indicates limited content)
**Current Analysis:** Partial sequences available

---

### Tablet G — Small Santiago

**File:** `tablet_G_recto.jpg` (337 KB)
**Description:** Smaller tablet from Santiago collection
**Referenced in Phase 3:** Boustrophedon pattern documented
**Key Features:** Clear glyph boundaries
**Current Analysis:** Available for topology studies

---

### Tablet H — Santiago Staff (Great Staff)

**Files:**
- `tablet_H_recto.jpg` (74 KB)
- `tablet_H_verso.jpg` (69 KB)

**Description:** Unique helical reading pattern, cylindrical staff format
**Referenced in Phase 3:** 2,320 glyphs continuous
**Referenced in Phase 6:** Bird enumeration pattern (P005) unique to this tablet
**Key Features:**
- Helical (spiral) reading direction
- B600-series bird catalog
- Longest continuous text

**Current Analysis:** Critical for understanding alternative reading patterns

---

### Tablet J

**File:** `tablet_J.jpg` (11 KB)
**Description:** Very small fragment or heavily damaged
**Key Features:** Limited content (small file size)
**Current Analysis:** Minimal data available

---

### Tablet K — Small London

**Files:**
- `tablet_K_recto.jpg` (61 KB)
- `tablet_K_verso.jpg` (196 KB)

**Description:** Small tablet with both surfaces
**Referenced in Phase 3:** Boustrophedon reading pattern
**Key Features:** Verso better preserved than recto
**Current Analysis:** Available for comparative studies

---

### Tablet L

**File:** `tablet_L.jpg` (108 KB)
**Description:** Single-surface or single-view documentation
**Key Features:** Moderate preservation
**Current Analysis:** Available for sequence extraction

---

### Tablet P — Large St. Petersburg

**File:** `tablet_P_recto.jpg` (387 KB)
**Description:** Large tablet from St. Petersburg collection
**Key Features:** Well-preserved, clear glyphs
**Current Analysis:** Suitable for detailed glyph analysis

---

### Tablet R — Small Washington

**Files:**
- `tablet_R_recto.jpg` (188 KB)
- `tablet_R_verso.jpg` (147 KB)

**Description:** Small tablet with both surfaces documented
**Key Features:** Both sides preserved
**Current Analysis:** Available for comparative studies

---

## Tablets Referenced in Phase 3 Topology Data

The following tablets have detailed line topology data in `corpus/topology/`:

1. **Tablet A** — Tahua (not yet photographed) — Largest known tablet
2. **Tablet B** — Aruku Kurenga ✅ **Photographed**
3. **Tablet C** — Mamari ✅ **Photographed** (both sides)
4. **Tablet G** — Small Santiago ✅ **Photographed**
5. **Tablet H** — Santiago Staff ✅ **Photographed** (helical pattern)
6. **Tablet K** — Small London ✅ **Photographed** (both sides)

**Coverage:** 5 of 6 tablets in topology analysis have photographs (83.3%)
**Missing:** Tablet A (Tahua) — largest tablet, topology data exists but no photo yet

---

## Notable Tablets Not Yet Photographed

Based on standard Barthel catalog:

- **Tablet A (Tahua)** — Critical, largest known tablet
- **Tablet I (Santiago Staff 2)** — Companion to Tablet H
- **Tablet M, N, O, Q, S, T, U, V, W, X, Y** — Various collections worldwide

---

## Usage Guidelines

### For Visual Analysis (Phase 1, 3)

1. Use photographs to verify glyph sequences in lexicon data
2. Confirm reading direction (boustrophedon vs. helical)
3. Identify line breaks and boundaries
4. Document physical damage or wear patterns

### For Topology Studies (Phase 3)

1. Cross-reference with `corpus/topology/tablet_lines.csv`
2. Verify rotation patterns (180° for boustrophedon)
3. Count glyphs per line for statistical validation
4. Confirm line start/end positions

### For Sequence Extraction (Phase 4, 6)

1. Extract actual glyph sequences for n-gram analysis
2. Identify parallel passages across tablets
3. Verify motif patterns documented in `banks/motifbank.json`
4. Support alignment atlas construction

### For Variant Analysis (Phase 2)

1. Compare glyph forms across different tablets
2. Identify scribal hands and variant styles
3. Document ligature appearances
4. Build variant-to-canonical mappings

---

## Image Quality Notes

- **High-resolution:** Tablets B, C, D, E, P, R (suitable for detailed glyph extraction)
- **Medium-resolution:** Tablets G, H, K, L (suitable for topology and sequence)
- **Low-resolution/Fragmentary:** Tablets F, J (limited analysis capability)

---

## Future Enhancements

1. **Tablet A Photography:** Acquire images of Tahua (largest tablet)
2. **Tablet Metadata:** Add provenance, museum location, catalog numbers
3. **Glyph-Level Annotations:** Create bounding boxes for individual glyphs
4. **Sequence Extraction Scripts:** Automated glyph recognition from photographs
5. **Comparative Views:** Side-by-side comparisons for variant analysis
6. **3D Scans:** If available, integrate depth data for wear analysis

---

## References

### Barthel Catalog System

Standard naming convention used by Thomas Barthel (1958):
- Letters A-Z identify individual tablets
- Recto/Verso or Side A/B distinguish surfaces
- Extensions (e.g., Fr1, Fr2) for fragments

### Cross-References

- **Phase 3 Topology:** `corpus/topology/tablet_metadata.csv`
- **Phase 6 Parallels:** Tablets with cross-references in `corpus/parallels/parallels.csv`
- **Phase 12 Calendar:** Tablet C (Mamari) lunar sequences in `banks/calendarbank.json`

---

## Attribution

**Photographs:** Public domain / museum collections (verify specific sources)
**Documentation:** Lackadaisical Security (The Operator)
**Catalog References:** Barthel (1958), Fischer, Pozdniakov, et al.

---

*"Visual evidence grounds all textual analysis. Every glyph interpretation begins with what we can see."*
