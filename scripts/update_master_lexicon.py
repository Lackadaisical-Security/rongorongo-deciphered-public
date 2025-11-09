#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update Master Lexicon

Copyright © 2025 Lackadaisical Security
Website: https://lackadaisical-security.com
Support: support@lackadaisical-security.com
GitHub: https://github.com/Lackadaisical-Security/rongorongo-deciphered-public

Licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
https://creativecommons.org/licenses/by-nc/4.0/

Update script to integrate 2025-09-26 MASTER lexicon
Expands from 306 to 734 glyph entries

Author: Lackadaisical Security (The Operator)
Created: 2025-10-30
Modified: 2025-10-30
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Lackadaisical Security"
__copyright__ = "Copyright © 2025 Lackadaisical Security"
__license__ = "CC BY-NC 4.0"


import json
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

# Repository paths
REPO_ROOT = Path(__file__).parent.parent
BANKS_DIR = REPO_ROOT / "banks"
ANALYSIS_DIR = REPO_ROOT / "analysis"
RUNS_DIR = REPO_ROOT / "runs"

def load_new_master():
    """Load the updated 2025-09-26 MASTER lexicon"""
    print("Loading updated MASTER lexicon (2025-09-26)...")
    
    with open(REPO_ROOT / "rongorongo_lexicon_MASTER_2025-09-26.updated.json", 'r') as f:
        master = json.load(f)
    
    print(f"  Loaded {len(master['lexicon'])} lexicon entries")
    print(f"  Version: {master['metadata']['version']}")
    print(f"  Total glyphs documented: {master['metadata']['total_glyphs']}")
    
    return master

def infer_contexts(english_meanings, notes, context_types):
    """Infer context types from meanings, notes, and existing context_types"""
    contexts = set()
    
    # Use existing context_types if available
    if context_types:
        contexts.update(context_types)
    
    # Common context patterns
    context_keywords = {
        'genealogical': ['genealog', 'ancestor', 'lineage', 'family', 'generation', 'descendant'],
        'astronomical': ['moon', 'sun', 'star', 'night', 'sky', 'celestial', 'lunar'],
        'calendrical': ['month', 'day', 'calendar', 'lunar', 'cycle', 'time', 'season'],
        'marine': ['fish', 'sea', 'ocean', 'water', 'marine', 'aquatic', 'turtle', 'shark'],
        'human_classification': ['person', 'human', 'man', 'woman', 'people', 'child', 'tangata'],
        'anatomical': ['body', 'head', 'eye', 'hand', 'arm', 'leg', 'face', 'mouth', 'ear'],
        'numerical': ['number', 'count', 'quantity', 'many', 'few', 'plural'],
        'ritual': ['sacred', 'ritual', 'ceremony', 'religious', 'spiritual', 'priest', 'god'],
        'social_hierarchy': ['chief', 'leader', 'rank', 'status', 'nobility', 'ariki'],
        'agricultural': ['plant', 'crop', 'harvest', 'cultivat', 'food', 'taro', 'yam'],
        'bird': ['bird', 'avian', 'wing', 'feather', 'fly', 'frigate', 'sooty tern'],
        'action': ['go', 'come', 'take', 'give', 'make', 'do', 'say', 'see'],
        'object': ['thing', 'object', 'tool', 'implement', 'house', 'canoe'],
    }
    
    # Combine meanings and notes for keyword search
    text = ' '.join(english_meanings if english_meanings else [])
    if notes:
        if isinstance(notes, list):
            text += ' ' + ' '.join(str(n) for n in notes)
        else:
            text += ' ' + str(notes)
    text = text.lower()
    
    for context_type, keywords in context_keywords.items():
        if any(kw in text for kw in keywords):
            contexts.add(context_type)
    
    # Default context if none found
    if not contexts:
        contexts.add('general')
    
    return list(contexts)

def create_updated_sensebank(master):
    """Create updated sensebank with 734 entries"""
    print("\nCreating updated sensebank...")
    
    sensebank = []
    
    for entry in master['lexicon']:
        glyph_id = str(entry['glyph_id'])
        english_meanings = entry.get('english_meanings', [])
        transliterations = entry.get('transliterations', [])
        confidence = entry.get('confidence', 0.5)
        notes = entry.get('notes', '')
        context_types = entry.get('context_types', [])
        
        # Infer contexts
        contexts = infer_contexts(english_meanings, notes, context_types)
        
        # Create sense entries (one per meaning, max 5)
        senses = []
        for i, meaning in enumerate(english_meanings[:5]):
            if not meaning:
                continue
            
            sense_id = meaning.lower().replace(' ', '_').replace(',', '').replace('/', '_').replace("'", '')[:30]
            
            # Estimate evidence based on confidence and position
            position_weight = 1.0 - (i * 0.1)
            
            sense_entry = {
                "id": sense_id,
                "meaning": meaning,
                "evidence": {
                    "freq": round(confidence * position_weight, 2),
                    "position": round(confidence * 0.9, 2),
                    "cluster": round(confidence * 0.8, 2),
                    "motif": round(confidence * (0.7 if i == 0 else 0.5), 2),
                    "parallel": round(confidence * 0.6, 2)
                },
                "confidence": round(confidence * position_weight, 2),
                "contexts": contexts
            }
            senses.append(sense_entry)
        
        # Create glyph entry
        glyph_entry = {
            "glyph": f"B{glyph_id.zfill(3)}" if glyph_id.isdigit() else glyph_id,
            "glyph_id": glyph_id,
            "transliterations": transliterations if transliterations else [],
            "senses": senses,
            "notes": notes if isinstance(notes, str) else str(notes),
            "source": entry.get('sources', ['Unknown'])[0] if entry.get('sources') else 'MASTER_2025-09-26',
            "tablets_found": entry.get('tablets_found', []),
            "occurrence_count": entry.get('occurrence_count', 0)
        }
        
        sensebank.append(glyph_entry)
    
    print(f"  Created {len(sensebank)} glyph entries")
    
    # Calculate statistics
    with_senses = sum(1 for g in sensebank if g['senses'])
    total_senses = sum(len(g['senses']) for g in sensebank)
    avg_senses = total_senses / with_senses if with_senses > 0 else 0
    
    print(f"  Glyphs with senses: {with_senses}")
    print(f"  Total sense entries: {total_senses}")
    print(f"  Average senses per glyph: {avg_senses:.2f}")
    
    return sensebank

def update_other_banks(sensebank):
    """Update namebank, calendarbank, etc. based on new sensebank"""
    print("\nUpdating specialized banks...")
    
    # NameBank - genealogical contexts
    namebank = []
    for entry in sensebank:
        contexts = []
        for sense in entry['senses']:
            contexts.extend(sense.get('contexts', []))
        
        if 'genealogical' in contexts or 'human_classification' in contexts:
            name_entry = {
                "glyph_sequence": [entry['glyph']],
                "transliteration": ' '.join(entry['transliterations']),
                "type": "personal_name_candidate",
                "contexts": list(set(contexts)),
                "confidence": max([s['confidence'] for s in entry['senses']]) if entry['senses'] else 0.5,
                "occurrence_count": entry.get('occurrence_count', 0),
                "tablets": entry.get('tablets_found', []),
                "notes": f"Appears in genealogical contexts: {entry['notes'][:100]}..."
            }
            namebank.append(name_entry)
    
    # CalendarBank - astronomical/calendrical contexts
    calendarbank = {
        "lunar_cycles": [],
        "month_names": [],
        "day_names": [],
        "temporal_markers": []
    }
    
    for entry in sensebank:
        contexts = []
        for sense in entry['senses']:
            contexts.extend(sense.get('contexts', []))
        
        if 'calendrical' in contexts or 'astronomical' in contexts:
            calendar_entry = {
                "glyph": entry['glyph'],
                "meanings": [s['meaning'] for s in entry['senses']],
                "transliteration": ' '.join(entry['transliterations']),
                "confidence": max([s['confidence'] for s in entry['senses']]) if entry['senses'] else 0.5,
                "occurrence_count": entry.get('occurrence_count', 0),
                "tablets": entry.get('tablets_found', []),
                "evidence": entry['notes']
            }
            
            meanings_str = ' '.join([s['meaning'].lower() for s in entry['senses']])
            if 'moon' in meanings_str or 'lunar' in meanings_str:
                calendarbank["lunar_cycles"].append(calendar_entry)
            elif 'month' in meanings_str:
                calendarbank["month_names"].append(calendar_entry)
            elif 'day' in meanings_str or 'night' in meanings_str:
                calendarbank["day_names"].append(calendar_entry)
            else:
                calendarbank["temporal_markers"].append(calendar_entry)
    
    # NumeralBank - numerical contexts
    numeralbank = {
        "numeral_glyphs": [],
        "counting_patterns": [],
        "quantifiers": []
    }
    
    for entry in sensebank:
        contexts = []
        meanings = []
        for sense in entry['senses']:
            contexts.extend(sense.get('contexts', []))
            meanings.append(sense['meaning'].lower())
        
        meanings_str = ' '.join(meanings)
        
        if 'numerical' in contexts or any(kw in meanings_str for kw in ['number', 'count', 'many', 'few', 'plural', 'quantity']):
            numeral_entry = {
                "glyph": entry['glyph'],
                "meanings": [s['meaning'] for s in entry['senses']],
                "transliteration": ' '.join(entry['transliterations']),
                "confidence": max([s['confidence'] for s in entry['senses']]) if entry['senses'] else 0.5,
                "occurrence_count": entry.get('occurrence_count', 0),
                "evidence": entry['notes']
            }
            numeralbank["numeral_glyphs"].append(numeral_entry)
    
    print(f"  NameBank: {len(namebank)} candidates")
    print(f"  CalendarBank: {sum(len(v) for v in calendarbank.values())} entries")
    print(f"  NumeralBank: {len(numeralbank['numeral_glyphs'])} numerals")
    
    return namebank, calendarbank, numeralbank

def main():
    """Main execution"""
    print("=" * 70)
    print("Rongorongo MASTER Lexicon Update (2025-09-26)")
    print("=" * 70)
    
    # Load new MASTER
    master = load_new_master()
    
    # Create updated sensebank
    sensebank = create_updated_sensebank(master)
    
    # Update other banks
    namebank, calendarbank, numeralbank = update_other_banks(sensebank)
    
    # Save files
    print("\nSaving updated files...")
    
    with open(BANKS_DIR / "sensebank.json", 'w') as f:
        json.dump(sensebank, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Updated {BANKS_DIR / 'sensebank.json'}")
    
    with open(BANKS_DIR / "namebank.json", 'w') as f:
        json.dump(namebank, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Updated {BANKS_DIR / 'namebank.json'}")
    
    with open(BANKS_DIR / "calendarbank.json", 'w') as f:
        json.dump(calendarbank, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Updated {BANKS_DIR / 'calendarbank.json'}")
    
    with open(BANKS_DIR / "numeralbank.json", 'w') as f:
        json.dump(numeralbank, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Updated {BANKS_DIR / 'numeralbank.json'}")
    
    # Create run metadata
    now = datetime.utcnow()
    run_id = now.strftime("%Y%m%d_%H%M%S")
    
    run_metadata = {
        "run_id": run_id,
        "timestamp": now.isoformat() + "Z",
        "phase": "master_lexicon_update_2025-09-26",
        "script_version": "2.0",
        "data_source": "rongorongo_lexicon_MASTER_2025-09-26.updated.json",
        "outputs": {
            "sensebank": f"{len(sensebank)} glyphs",
            "namebank": f"{len(namebank)} candidates",
            "calendarbank": f"{sum(len(v) for v in calendarbank.values())} entries",
            "numeralbank": f"{len(numeralbank['numeral_glyphs'])} numerals"
        },
        "improvements": {
            "previous_glyphs": 306,
            "new_glyphs": len(sensebank),
            "increase": len(sensebank) - 306
        }
    }
    
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    with open(run_dir / "run.json", 'w') as f:
        json.dump(run_metadata, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Saved {run_dir / 'run.json'}")
    
    print("\n" + "=" * 70)
    print("✓ MASTER lexicon update complete!")
    print("=" * 70)
    print(f"\nSummary:")
    print(f"  - Expanded from 306 to {len(sensebank)} glyphs (+{len(sensebank)-306})")
    print(f"  - {len(namebank)} name candidates (genealogical contexts)")
    print(f"  - {sum(len(v) for v in calendarbank.values())} calendar entries")
    print(f"  - {len(numeralbank['numeral_glyphs'])} numeral candidates")
    print(f"\nRun ID: {run_id}")

if __name__ == "__main__":
    main()
