#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate Data

Copyright © 2025 Lackadaisical Security
Website: https://lackadaisical-security.com
Support: support@lackadaisical-security.com
GitHub: https://github.com/Lackadaisical-Security/rongorongo-deciphered-public

Licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
https://creativecommons.org/licenses/by-nc/4.0/

Validation script for Phase 1-20 data
Ensures all bank files are properly formatted and internally consistent

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

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

REPO_ROOT = Path(__file__).parent.parent
BANKS_DIR = REPO_ROOT / "banks"
ANALYSIS_DIR = REPO_ROOT / "analysis"

def validate_sensebank():
    """Validate sensebank.json structure and content"""
    print("Validating sensebank.json...")

    with open(BANKS_DIR / "sensebank.json", 'r', encoding='utf-8') as f:
        sensebank = json.load(f)
    
    errors = []
    warnings = []
    
    # Check it's a list
    if not isinstance(sensebank, list):
        errors.append("SenseBank must be a list")
        return errors, warnings
    
    # Validate each entry
    required_fields = ['glyph', 'glyph_id', 'transliterations', 'senses', 'notes', 'source']
    sense_fields = ['id', 'meaning', 'evidence', 'confidence', 'contexts']
    evidence_fields = ['freq', 'position', 'cluster', 'motif', 'parallel']
    
    for i, entry in enumerate(sensebank):
        # Check required fields
        for field in required_fields:
            if field not in entry:
                errors.append(f"Entry {i} missing required field: {field}")
        
        # Check senses
        if 'senses' in entry:
            if not isinstance(entry['senses'], list):
                errors.append(f"Entry {i}: senses must be a list")
            elif len(entry['senses']) == 0:
                warnings.append(f"Entry {i} ({entry.get('glyph', '?')}): no senses defined")
            elif len(entry['senses']) > 5:
                warnings.append(f"Entry {i} ({entry.get('glyph', '?')}): >5 senses (methodology suggests 3-5)")
            
            for j, sense in enumerate(entry['senses']):
                for field in sense_fields:
                    if field not in sense:
                        errors.append(f"Entry {i}, sense {j}: missing field {field}")
                
                # Check evidence
                if 'evidence' in sense:
                    for efield in evidence_fields:
                        if efield not in sense['evidence']:
                            errors.append(f"Entry {i}, sense {j}: evidence missing {efield}")
                
                # Check confidence range
                if 'confidence' in sense:
                    conf = sense['confidence']
                    if not (0.0 <= conf <= 1.0):
                        errors.append(f"Entry {i}, sense {j}: confidence {conf} out of range [0,1]")
    
    print(f"  Total entries: {len(sensebank)}")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    
    return errors, warnings

def validate_namebank():
    """Validate namebank.json structure"""
    print("\nValidating namebank.json...")

    with open(BANKS_DIR / "namebank.json", 'r', encoding='utf-8') as f:
        namebank = json.load(f)
    
    errors = []
    warnings = []
    
    required_fields = ['glyph_sequence', 'transliteration', 'type', 'contexts', 'confidence', 'notes']
    
    for i, entry in enumerate(namebank):
        for field in required_fields:
            if field not in entry:
                errors.append(f"Entry {i}: missing field {field}")
        
        if 'confidence' in entry:
            conf = entry['confidence']
            if not (0.0 <= conf <= 1.0):
                errors.append(f"Entry {i}: confidence {conf} out of range [0,1]")
    
    print(f"  Total entries: {len(namebank)}")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    
    return errors, warnings

def validate_calendarbank():
    """Validate calendarbank.json structure"""
    print("\nValidating calendarbank.json...")

    with open(BANKS_DIR / "calendarbank.json", 'r', encoding='utf-8') as f:
        calendarbank = json.load(f)
    
    errors = []
    warnings = []
    
    required_keys = ['lunar_cycles', 'month_names', 'day_names', 'temporal_markers']
    
    for key in required_keys:
        if key not in calendarbank:
            errors.append(f"Missing required key: {key}")
    
    total = sum(len(calendarbank[k]) for k in required_keys if k in calendarbank)
    
    print(f"  Total entries: {total}")
    print(f"  - Lunar cycles: {len(calendarbank.get('lunar_cycles', []))}")
    print(f"  - Month names: {len(calendarbank.get('month_names', []))}")
    print(f"  - Day names: {len(calendarbank.get('day_names', []))}")
    print(f"  - Temporal markers: {len(calendarbank.get('temporal_markers', []))}")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    
    return errors, warnings

def validate_numeralbank():
    """Validate numeralbank.json structure"""
    print("\nValidating numeralbank.json...")

    with open(BANKS_DIR / "numeralbank.json", 'r', encoding='utf-8') as f:
        numeralbank = json.load(f)
    
    errors = []
    warnings = []
    
    required_keys = ['numeral_glyphs', 'counting_patterns', 'quantifiers']
    
    for key in required_keys:
        if key not in numeralbank:
            errors.append(f"Missing required key: {key}")
    
    total = sum(len(numeralbank[k]) for k in required_keys if k in numeralbank)
    
    print(f"  Total entries: {total}")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    
    return errors, warnings

def validate_motifbank():
    """Validate motifbank.json structure"""
    print("\nValidating motifbank.json...")

    with open(BANKS_DIR / "motifbank.json", 'r', encoding='utf-8') as f:
        motifbank = json.load(f)
    
    errors = []
    warnings = []
    
    required_fields = ['motif_id', 'parts', 'support', 'tablets', 'grade']
    
    for i, entry in enumerate(motifbank):
        for field in required_fields:
            if field not in entry:
                errors.append(f"Entry {i}: missing field {field}")
        
        if 'grade' in entry:
            grade = entry['grade']
            if grade not in ['A', 'B', 'C', 'D']:
                warnings.append(f"Entry {i}: unusual grade {grade} (expected A-D)")
    
    print(f"  Total entries: {len(motifbank)}")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    
    return errors, warnings

def validate_clusters():
    """Validate clusters.json structure"""
    print("\nValidating clusters.json...")

    with open(ANALYSIS_DIR / "clusters.json", 'r', encoding='utf-8') as f:
        clusters = json.load(f)
    
    errors = []
    warnings = []
    
    required_fields = ['id', 'label', 'members', 'size', 'modularity', 'stability']
    
    for cluster_id, cluster in clusters.items():
        for field in required_fields:
            if field not in cluster:
                errors.append(f"Cluster {cluster_id}: missing field {field}")
        
        if 'modularity' in cluster:
            mod = cluster['modularity']
            if not (0.0 <= mod <= 1.0):
                warnings.append(f"Cluster {cluster_id}: modularity {mod} out of typical range [0,1]")
        
        if 'stability' in cluster:
            stab = cluster['stability']
            if not (0.0 <= stab <= 1.0):
                warnings.append(f"Cluster {cluster_id}: stability {stab} out of range [0,1]")
    
    print(f"  Total clusters: {len(clusters)}")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    
    return errors, warnings

def validate_constraints():
    """Validate constraints.json structure"""
    print("\nValidating constraints.json...")

    with open(ANALYSIS_DIR / "constraints.json", 'r', encoding='utf-8') as f:
        constraints = json.load(f)
    
    errors = []
    warnings = []
    
    required_keys = ['phonotactic_rules', 'cultural_constraints', 'structural_constraints']
    
    for key in required_keys:
        if key not in constraints:
            errors.append(f"Missing required key: {key}")
    
    print(f"  Constraint categories: {len(constraints)}")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    
    return errors, warnings

def main():
    """Run all validations"""
    print("=" * 70)
    print("Rongorongo Phase 1-20 Data Validation")
    print("=" * 70)
    
    all_errors = []
    all_warnings = []
    
    # Validate each bank
    validators = [
        validate_sensebank,
        validate_namebank,
        validate_calendarbank,
        validate_numeralbank,
        validate_motifbank,
        validate_clusters,
        validate_constraints
    ]
    
    for validator in validators:
        try:
            errors, warnings = validator()
            all_errors.extend(errors)
            all_warnings.extend(warnings)
        except Exception as e:
            all_errors.append(f"Validation error in {validator.__name__}: {e}")
    
    # Summary
    print("\n" + "=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)
    print(f"Total Errors: {len(all_errors)}")
    print(f"Total Warnings: {len(all_warnings)}")
    
    if all_errors:
        print("\n❌ ERRORS:")
        for error in all_errors:
            print(f"  - {error}")
    
    if all_warnings:
        print("\n⚠️  WARNINGS:")
        for warning in all_warnings:
            print(f"  - {warning}")
    
    if not all_errors and not all_warnings:
        print("\n✅ All validations passed!")
        return 0
    elif not all_errors:
        print("\n✅ No errors, but some warnings present")
        return 0
    else:
        print("\n❌ Validation failed with errors")
        return 1

if __name__ == "__main__":
    sys.exit(main())
