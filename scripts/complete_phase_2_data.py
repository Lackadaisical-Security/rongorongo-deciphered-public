#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete Phase 2 Data

Copyright © 2025 Lackadaisical Security
Website: https://lackadaisical-security.com
Support: support@lackadaisical-security.com
GitHub: https://github.com/Lackadaisical-Security/rongorongo-deciphered-public

Licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
https://creativecommons.org/licenses/by-nc/4.0/

Complete Phase 2 Data: Variant & Ligature Discipline
Creates detailed CSV files for variants and ligatures

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
import csv
import os
from datetime import datetime

def load_sensebank():
    """Load the sensebank data"""
    with open('banks/sensebank.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_variant_mappings(sensebank):
    """Extract canonical↔variant mappings from glyph data"""
    variants = []
    
    # Group glyphs by their base form
    glyph_families = {}
    for entry in sensebank:
        glyph = entry.get('glyph', '')
        if not glyph:
            continue
            
        # Extract base form (e.g., B001 from B001a, B001.1, etc.)
        base = glyph[:4] if len(glyph) >= 4 else glyph
        
        # Check for variant indicators (suffixes, dots, etc.)
        is_variant = (
            len(glyph) > 4 or 
            '.' in glyph or 
            glyph[-1].isalpha() and len(glyph) > 4
        )
        
        if base not in glyph_families:
            glyph_families[base] = {
                'canonical': base,
                'variants': []
            }
        
        if is_variant:
            glyph_families[base]['variants'].append(glyph)
    
    # Create variant mappings
    for base, family in glyph_families.items():
        canonical = family['canonical']
        for variant in family['variants']:
            variants.append({
                'canonical_form': canonical,
                'variant_form': variant,
                'relationship': 'graphemic_variant',
                'confidence': 0.75,
                'notes': 'Identified from glyph ID structure'
            })
    
    return variants

def extract_ligature_mappings(sensebank):
    """Extract ligature decompositions from glyph data"""
    ligatures = []
    
    for entry in sensebank:
        glyph = entry.get('glyph', '')
        senses = entry.get('senses', [])
        
        # Look for composite meanings or descriptions suggesting ligatures
        for sense in senses:
            meaning = sense.get('meaning', '').lower()
            
            # Heuristic: look for compound descriptions
            if any(indicator in meaning for indicator in ['+', 'with', 'and', 'combined', 'composite']):
                # Try to extract components
                components = []
                
                # Simple heuristic for now - can be enhanced
                if '+' in meaning:
                    parts = meaning.split('+')
                    components = [p.strip() for p in parts]
                
                if len(components) >= 2:
                    ligatures.append({
                        'ligature_glyph': glyph,
                        'component_1': components[0][:20],  # Limit length
                        'component_2': components[1][:20] if len(components) > 1 else '',
                        'component_3': components[2][:20] if len(components) > 2 else '',
                        'confidence': 0.6,
                        'decomposition_type': 'semantic_composite',
                        'notes': f'From meaning: {meaning[:50]}'
                    })
                    break  # Only one ligature per glyph
    
    return ligatures

def create_variant_csv():
    """Create variants.csv with all variant mappings"""
    print('  Creating variants.csv...')
    
    sensebank = load_sensebank()
    variants = extract_variant_mappings(sensebank)
    
    os.makedirs('corpus/variants', exist_ok=True)
    
    with open('corpus/variants/variants.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['canonical_form', 'variant_form', 'relationship', 'confidence', 'notes']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(variants)
    
    print(f'    Created variants.csv with {len(variants)} mappings')
    return len(variants)

def create_ligatures_csv():
    """Create ligatures.csv with composite decompositions"""
    print('  Creating ligatures.csv...')
    
    sensebank = load_sensebank()
    ligatures = extract_ligature_mappings(sensebank)
    
    os.makedirs('corpus/variants', exist_ok=True)
    
    with open('corpus/variants/ligatures.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['ligature_glyph', 'component_1', 'component_2', 'component_3', 
                     'confidence', 'decomposition_type', 'notes']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(ligatures)
    
    print(f'    Created ligatures.csv with {len(ligatures)} decompositions')
    return len(ligatures)

def create_verification_data():
    """Create round-trip verification metadata"""
    print('  Creating verification metadata...')
    
    verification = {
        'metadata': {
            'created': datetime.now().isoformat(),
            'phase': 2,
            'title': 'Variant & Ligature Verification'
        },
        'verification_tests': [
            {
                'test_name': 'variant_bidirectionality',
                'description': 'Verify all variants map correctly to canonical forms',
                'status': 'defined',
                'criteria': 'Each variant must map to exactly one canonical form'
            },
            {
                'test_name': 'ligature_completeness',
                'description': 'Verify all ligature components exist in corpus',
                'status': 'defined',
                'criteria': 'Each component must be a valid glyph or semantic concept'
            },
            {
                'test_name': 'consistency_check',
                'description': 'Verify no conflicts in variant/canonical assignments',
                'status': 'defined',
                'criteria': 'No glyph should be both canonical and variant simultaneously'
            }
        ],
        'quality_metrics': {
            'variant_coverage': 'To be calculated from corpus',
            'ligature_confidence_avg': 0.6,
            'manual_review_required': True
        }
    }
    
    with open('corpus/variants/verification.json', 'w', encoding='utf-8') as f:
        json.dump(verification, f, indent=2, ensure_ascii=False)
    
    print('    Created verification.json')

def main():
    print('Completing Phase 2: Variant & Ligature Discipline')
    print('=' * 50)
    
    variant_count = create_variant_csv()
    ligature_count = create_ligatures_csv()
    create_verification_data()
    
    print('\nPhase 2 Data Complete:')
    print(f'  - {variant_count} variant mappings')
    print(f'  - {ligature_count} ligature decompositions')
    print('  - Verification framework defined')

if __name__ == '__main__':
    main()
