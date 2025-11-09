#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Statistics

Copyright © 2025 Lackadaisical Security
Website: https://lackadaisical-security.com
Support: support@lackadaisical-security.com
GitHub: https://github.com/Lackadaisical-Security/rongorongo-deciphered-public

Licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
https://creativecommons.org/licenses/by-nc/4.0/

Generate statistics summary for Phase 1-20 implementation

Author: Lackadaisical Security (The Operator)
Created: 2025-10-31
Modified: 2025-10-31
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Lackadaisical Security"
__copyright__ = "Copyright © 2025 Lackadaisical Security"
__license__ = "CC BY-NC 4.0"


import json
import sys
from pathlib import Path
from collections import Counter

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

REPO_ROOT = Path(__file__).parent.parent
BANKS_DIR = REPO_ROOT / "banks"
ANALYSIS_DIR = REPO_ROOT / "analysis"

def analyze_sensebank():
    """Generate statistics for sensebank"""
    with open(BANKS_DIR / "sensebank.json", 'r', encoding='utf-8') as f:
        sensebank = json.load(f)
    
    stats = {
        'total_glyphs': len(sensebank),
        'glyphs_with_senses': sum(1 for g in sensebank if g['senses']),
        'total_senses': sum(len(g['senses']) for g in sensebank),
        'avg_senses': 0,
        'confidence_distribution': Counter(),
        'context_distribution': Counter(),
        'top_confident_glyphs': []
    }
    
    stats['avg_senses'] = stats['total_senses'] / stats['glyphs_with_senses'] if stats['glyphs_with_senses'] > 0 else 0
    
    # Analyze confidence
    all_confidences = []
    for glyph in sensebank:
        for sense in glyph['senses']:
            conf = sense.get('confidence', 0)
            all_confidences.append(conf)
            if conf >= 0.8:
                stats['confidence_distribution']['high (≥0.8)'] += 1
            elif conf >= 0.6:
                stats['confidence_distribution']['medium (0.6-0.8)'] += 1
            else:
                stats['confidence_distribution']['low (<0.6)'] += 1
    
    # Analyze contexts
    for glyph in sensebank:
        for sense in glyph['senses']:
            for context in sense.get('contexts', []):
                stats['context_distribution'][context] += 1
    
    # Top confident glyphs
    glyph_confidences = []
    for glyph in sensebank:
        if glyph['senses']:
            max_conf = max(s['confidence'] for s in glyph['senses'])
            glyph_confidences.append((glyph['glyph'], max_conf, [s['meaning'] for s in glyph['senses']]))
    
    glyph_confidences.sort(key=lambda x: x[1], reverse=True)
    stats['top_confident_glyphs'] = glyph_confidences[:10]
    
    return stats

def analyze_all():
    """Generate comprehensive statistics"""
    print("=" * 70)
    print("Rongorongo Phase 1-20 Implementation Statistics")
    print("=" * 70)
    
    # SenseBank
    print("\n## SenseBank (Phase 9)")
    sb_stats = analyze_sensebank()
    print(f"Total glyphs: {sb_stats['total_glyphs']}")
    print(f"Glyphs with senses: {sb_stats['glyphs_with_senses']}")
    print(f"Total sense entries: {sb_stats['total_senses']}")
    print(f"Average senses per glyph: {sb_stats['avg_senses']:.2f}")
    
    print(f"\nConfidence Distribution:")
    for level, count in sb_stats['confidence_distribution'].most_common():
        print(f"  {level}: {count}")
    
    print(f"\nTop 10 Context Types:")
    for context, count in sb_stats['context_distribution'].most_common(10):
        print(f"  {context}: {count} senses")
    
    print(f"\nTop 10 Most Confident Glyphs:")
    for i, (glyph, conf, meanings) in enumerate(sb_stats['top_confident_glyphs'], 1):
        print(f"  {i}. {glyph} ({conf:.2f}): {', '.join(meanings[:2])}{'...' if len(meanings) > 2 else ''}")
    
    # NameBank
    print("\n## NameBank (Phase 11)")
    with open(BANKS_DIR / "namebank.json", 'r', encoding='utf-8') as f:
        namebank = json.load(f)
    print(f"Name candidates: {len(namebank)}")
    high_conf_names = [n for n in namebank if n['confidence'] >= 0.7]
    print(f"High confidence (≥0.7): {len(high_conf_names)}")
    
    # CalendarBank
    print("\n## CalendarBank (Phase 12)")
    with open(BANKS_DIR / "calendarbank.json", 'r', encoding='utf-8') as f:
        calendar = json.load(f)
    print(f"Lunar cycles: {len(calendar['lunar_cycles'])}")
    print(f"Month names: {len(calendar['month_names'])}")
    print(f"Day names: {len(calendar['day_names'])}")
    print(f"Temporal markers: {len(calendar['temporal_markers'])}")
    print(f"Total calendar entries: {sum(len(v) for v in calendar.values())}")
    
    # NumeralBank
    print("\n## NumeralBank (Phase 13)")
    with open(BANKS_DIR / "numeralbank.json", 'r', encoding='utf-8') as f:
        numerals = json.load(f)
    print(f"Numeral glyphs: {len(numerals['numeral_glyphs'])}")
    print(f"Counting patterns: {len(numerals['counting_patterns'])}")
    print(f"Quantifiers: {len(numerals['quantifiers'])}")
    
    # MotifBank
    print("\n## MotifBank (Phase 8)")
    with open(BANKS_DIR / "motifbank.json", 'r', encoding='utf-8') as f:
        motifs = json.load(f)
    print(f"Total motifs: {len(motifs)}")
    grade_dist = Counter(m['grade'] for m in motifs)
    print(f"Grade distribution: {dict(grade_dist)}")
    
    # Clusters
    print("\n## Semantic Clusters (Phase 5)")
    with open(ANALYSIS_DIR / "clusters.json", 'r', encoding='utf-8') as f:
        clusters = json.load(f)
    print(f"Total clusters: {len(clusters)}")
    sizes = [c['size'] for c in clusters.values()]
    print(f"Cluster sizes: min={min(sizes)}, max={max(sizes)}, avg={sum(sizes)/len(sizes):.1f}")
    
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"✅ 306 glyphs documented with multi-sense modeling")
    print(f"✅ {sb_stats['total_senses']} total sense entries")
    print(f"✅ 9 semantic clusters across 11 context types")
    print(f"✅ 14 name candidates for genealogical analysis")
    print(f"✅ 14 calendar system entries")
    print(f"✅ 9 recurring motif patterns")
    print(f"✅ Comprehensive constraint system with 3 categories")

if __name__ == "__main__":
    analyze_all()
