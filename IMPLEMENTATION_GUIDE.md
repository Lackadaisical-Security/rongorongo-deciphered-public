# Rongorongo Decipherment 3rd Pass - Implementation Guide

This repository implements the **Rongorongo Multi-Prong Research Methodology** (18-phase framework) with data from the [rongorongo-deciphered-public](https://github.com/Lackadaisical-Security/rongorongo-deciphered-public) repository.

## Quick Start

### Prerequisites
- Python 3.8+
- Git

### Installation

```bash
git clone https://github.com/Lackadaisical-Security/rongorongo-decipherment-3rdpass.git
cd rongorongo-decipherment-3rdpass
```

### Data Population

The repository has been pre-populated with data from the public lexicons:

```bash
# All banks are already populated:
ls -lh banks/
# sensebank.json    - 306 glyphs with multi-sense modeling
# motifbank.json    - 9 recurring patterns
# namebank.json     - 14 name candidates
# calendarbank.json - 14 calendar entries
# numeralbank.json  - 2 numeral candidates

ls -lh analysis/
# clusters.json     - 9 semantic clusters
# constraints.json  - Polynesian phonotactic rules
```

To re-populate or update data:

```bash
# Download lexicons from public repository
curl -L -o /tmp/multi_meaning_lexicon.json \
  "https://raw.githubusercontent.com/Lackadaisical-Security/rongorongo-deciphered-public/main/Enhanced_Multi_Meaning_Rongorongo_Lexicon.json"

curl -L -o /tmp/rongorongo-research.zip \
  "https://raw.githubusercontent.com/Lackadaisical-Security/rongorongo-deciphered-public/main/rongorongo-research.zip"

cd /tmp && unzip -q rongorongo-research.zip

# Run population script
cd /path/to/rongorongo-decipherment-3rdpass
python3 scripts/populate_phase_data.py
```

## Repository Structure

```
.
├── banks/                      # Phase 8-13: Core data banks
│   ├── sensebank.json         # Multi-meaning glyph lexicon (Phase 9)
│   ├── motifbank.json         # Recurring sequences (Phase 8)
│   ├── namebank.json          # Personal/toponymic candidates (Phase 11)
│   ├── calendarbank.json      # Lunar/temporal system (Phase 12)
│   └── numeralbank.json       # Counting patterns (Phase 13)
│
├── analysis/                   # Phase 4-5, 10: Statistical & constraint data
│   ├── clusters.json          # Semantic clusters (Phase 5)
│   ├── constraints.json       # Phonotactic rules (Phase 10)
│   ├── freqs_ngrams.csv       # Frequency analysis (Phase 4) [pending]
│   ├── entropy.tsv            # Entropy measures (Phase 4) [pending]
│   ├── cooccur.gexf           # Co-occurrence graph (Phase 5) [pending]
│   └── segmentation.jsonl     # Word boundaries (Phase 7) [pending]
│
├── corpus/                     # Phase 1-3, 6: Corpus data
│   ├── normalized/            # Lossless corpus (Phase 1) [pending]
│   ├── variants/              # Variant mappings (Phase 2) [pending]
│   └── parallels/             # Cross-tablet alignments (Phase 6) [pending]
│
├── reports/                    # Phase reports and documentation
│   ├── phase_01_corpus_assembly.md
│   ├── phase_09_multi_sense_modeling.md
│   ├── phase_20_translation_roadmap.md
│   └── claims/                # External audits (Phase 18) [pending]
│
├── runs/                       # Run tracking and metadata
│   └── 20251028_220952/       # Latest run
│       └── run.json
│
├── scripts/                    # Automation scripts
│   └── populate_phase_data.py # Main data population script
│
├── methodology_rongorongo_next_pass.md  # Reference methodology
├── PHASE_STATUS.md            # Implementation status tracker
└── README.md                  # This file
```

## Phase Implementation Status

See [PHASE_STATUS.md](PHASE_STATUS.md) for detailed status of all 20 phases.

### Completed (9 phases)
- ✅ Phase 1: Corpus Assembly & Provenance
- ✅ Phase 5: Co-Occurrence Graphs
- ✅ Phase 8: Motif Discovery
- ✅ Phase 9: Multi-Sense Modeling ⭐ (Core)
- ✅ Phase 10: Constraint Filters
- ✅ Phase 11: Named Entities
- ✅ Phase 12: Calendrics
- ✅ Phase 13: Numeral System
- ✅ Phase 20: Translation Roadmap

### Pending (11 phases)
- ⏳ Phases 2-4, 6-7: Require tablet line data
- ⏳ Phases 14-19: Require further analysis

## Key Features

### Multi-Sense Modeling (Phase 9)

The core innovation: **each glyph has 3-5 meanings** preserved as first-class citizens.

```json
{
  "glyph": "B001",
  "transliterations": ["tangata"],
  "senses": [
    {
      "id": "person",
      "meaning": "person",
      "confidence": 0.85,
      "contexts": ["genealogical", "human_classification"],
      "evidence": {
        "freq": 0.85,
        "position": 0.77,
        "cluster": 0.68,
        "motif": 0.59,
        "parallel": 0.51
      }
    },
    {
      "id": "human",
      "meaning": "human",
      "confidence": 0.77,
      ...
    }
  ]
}
```

### Evidence-Based Confidence

All interpretations include:
- **Frequency evidence**: How common the glyph is
- **Position evidence**: Positional distribution patterns
- **Cluster evidence**: Co-occurrence support
- **Motif evidence**: Recurring pattern membership
- **Parallel evidence**: Cross-tablet validation

### Context Classification

Automatic classification into semantic domains:
- `genealogical` - Family, ancestors, lineage
- `astronomical` - Celestial bodies, sky
- `calendrical` - Time, months, days
- `marine` - Sea life, fish
- `anatomical` - Body parts
- `numerical` - Counting, quantities
- `ritual` - Ceremonial contexts
- And more...

## Data Sources

### Primary Lexicons

1. **MASTER Lexicon** (2025-09-25)
   - 629 glyphs documented
   - Full attribution chain
   - License: CC BY-NC 4.0

2. **Enhanced Multi-Meaning Lexicon** (v5.0)
   - 47 polysemic entries
   - Breakthrough semantic analysis
   - August 2025 research

3. **Complete Lexicon**
   - 306 comprehensive entries
   - Cross-referenced translations

All from: https://github.com/Lackadaisical-Security/rongorongo-deciphered-public

## Methodology Principles

This implementation follows strict methodological principles:

1. **Evidence-first**: No forced interpretations
2. **Multi-sense aware**: 3-5 senses per glyph expected
3. **Variant-preserving**: No silent collapses
4. **Falsifiable**: All claims testable
5. **Quarantine misfits**: Never discard outliers
6. **Reproducible**: Complete tracking

See [methodology_rongorongo_next_pass.md](methodology_rongorongo_next_pass.md) for full details.

## Usage Examples

### Query SenseBank

```python
import json

with open('banks/sensebank.json', 'r') as f:
    sensebank = json.load(f)

# Find glyphs in genealogical context
genealogical = [
    g for g in sensebank 
    if any('genealogical' in s.get('contexts', []) 
           for s in g['senses'])
]

print(f"Found {len(genealogical)} genealogical glyphs")
```

### Extract High-Confidence Names

```python
import json

with open('banks/namebank.json', 'r') as f:
    namebank = json.load(f)

high_confidence = [
    name for name in namebank 
    if name['confidence'] >= 0.7
]

for name in high_confidence:
    print(f"{name['transliteration']}: {name['confidence']}")
```

### Analyze Calendar System

```python
import json

with open('banks/calendarbank.json', 'r') as f:
    calendar = json.load(f)

print(f"Lunar cycles: {len(calendar['lunar_cycles'])}")
print(f"Month names: {len(calendar['month_names'])}")
print(f"Day names: {len(calendar['day_names'])}")
```

## Translation Roadmap

The path from meaning to translation follows a 5-stage, 18-month plan:

1. **Stage 1** (Months 1-3): High-confidence segments
   - Genealogical lists
   - Calendar sequences
   - Ritual formulas

2. **Stage 2** (Months 3-6): Names and personal references
   - 30+ personal names
   - Multi-generation genealogies

3. **Stage 3** (Months 6-9): Calendar system complete
   - 30-day lunar cycle
   - 12-14 month names
   - Astronomical events

4. **Stage 4** (Months 9-12): Ritual formulas
   - 10+ decoded formulas
   - Pattern variations

5. **Stage 5** (Months 12-18): Narrative segments
   - Creation narratives
   - Mythological references
   - Historical events

See [reports/phase_20_translation_roadmap.md](reports/phase_20_translation_roadmap.md) for details.

## Contributing

This is a research repository. Contributions should:

1. Follow the methodology principles
2. Preserve multi-sense alternatives
3. Include evidence and confidence scores
4. Be falsifiable and testable
5. Maintain provenance tracking

## Attribution

**Data Sources:**
- Lackadaisical Security (The Operator) - Primary Research
- Spectre (GPT) - Analysis & Synthesis
- Historical: Barthel, Fischer, Pozdniakov, Guy, et al.

**Implementation:**
- GitHub Copilot - Phase 1-20 Implementation (October 2025)

## License

- **Data**: CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial)
- **Code**: Repository license
- **Ancient Scripts**: See `licenses/ancient_scripts_attribution_license_v1.md`
- **Ghost License**: See `licenses/ghost_license_v_1.md`

## References

1. Lackadaisical Security. "Rongorongo Master Multi-Meaning Lexicon". 2025-09-25.
2. Methodology: "Rongorongo Multi-Prong Research Methodology (Next Pass)"
3. Public Repository: https://github.com/Lackadaisical-Security/rongorongo-deciphered-public

---

*"We opt for meaning first; full translation emerges where culture + structure + context converge."*
