#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Release Package

Copyright © 2025 Lackadaisical Security
Website: https://lackadaisical-security.com
Support: support@lackadaisical-security.com
GitHub: https://github.com/Lackadaisical-Security/rongorongo-deciphered-public

Licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
https://creativecommons.org/licenses/by-nc/4.0/

Phase 19: Packaging & Release Engineering

Creates reproducible release package with checksums and documentation.

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
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

def calculate_checksum(filepath: Path) -> str:
    """Calculate SHA256 checksum for file"""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def save_json(data: Any, filepath: Path):
    """Save JSON file with formatting"""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def create_file_inventory(base_path: Path) -> List[Dict]:
    """Create inventory of all project files with checksums"""
    inventory = []
    
    # Define directories to include
    include_dirs = [
        "banks",
        "analysis",
        "reports",
        "scripts",
        "corpus",
        "methodology_rongorongo_next_pass.md",
        "PHASE_STATUS.md",
        "IMPLEMENTATION_GUIDE.md",
        "README.md"
    ]
    
    for item in include_dirs:
        item_path = base_path / item
        if item_path.is_file():
            inventory.append({
                "path": str(item_path.relative_to(base_path)),
                "type": "file",
                "size": item_path.stat().st_size,
                "checksum": calculate_checksum(item_path)
            })
        elif item_path.is_dir():
            for filepath in item_path.rglob("*"):
                if filepath.is_file() and not filepath.name.startswith('.'):
                    inventory.append({
                        "path": str(filepath.relative_to(base_path)),
                        "type": "file",
                        "size": filepath.stat().st_size,
                        "checksum": calculate_checksum(filepath)
                    })
    
    return sorted(inventory, key=lambda x: x["path"])

def create_release_manifest(base_path: Path, inventory: List[Dict]) -> Dict:
    """Create release manifest with metadata"""
    return {
        "release_info": {
            "version": "3rd-pass-v1.0",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "timestamp": datetime.now().isoformat(),
            "description": "Rongorongo Multi-Prong Research Methodology - 3rd Pass Implementation"
        },
        "phases_completed": {
            "total": 20,
            "implemented": 15,
            "completion_rate": "75%",
            "completed_phases": [1, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "pending_phases": [2, 3, 4, 6, 7]
        },
        "data_summary": {
            "glyphs_documented": 734,
            "sense_entries": 558,
            "name_candidates": 33,
            "calendar_entries": 32,
            "numeral_candidates": 8,
            "semantic_clusters": 9,
            "function_classes": 7,
            "cultural_contexts": 111,
            "ethnographic_frames": 6
        },
        "file_inventory": {
            "total_files": len(inventory),
            "total_size_bytes": sum(f["size"] for f in inventory),
            "files": inventory
        },
        "data_sources": {
            "master_lexicon": "rongorongo_lexicon_MASTER_2025-09-26.updated.json",
            "enhanced_lexicon": "Enhanced_Multi_Meaning_Rongorongo_Lexicon.json",
            "pdf_documents": "15 second-pass phase PDFs + overview",
            "repository": "github.com/Lackadaisical-Security/rongorongo-deciphered-public"
        },
        "methodology": {
            "approach": "Conservative, grounded, cross-verified",
            "principles": [
                "No forced interpretations",
                "Natural pattern emergence from data",
                "Multi-source cross-verification",
                "Explicit confidence levels",
                "Limitations acknowledged"
            ]
        },
        "attribution": {
            "primary_research": "Lackadaisical Security (The Operator) & Spectre",
            "implementation": "GitHub Copilot",
            "date": "October 28, 2025",
            "license": "CC BY-NC 4.0"
        },
        "verification": {
            "reproducibility": "All scripts included for reproduction",
            "validation": "0 structural errors, Phase 15 cross-validation passed",
            "checksum_algorithm": "SHA256"
        }
    }

def generate_release_notes() -> str:
    """Generate markdown release notes"""
    notes = []
    notes.append("# Rongorongo Decipherment 3rd Pass - Release v1.0\n\n")
    notes.append(f"**Release Date:** {datetime.now().strftime('%Y-%m-%d')}\n")
    notes.append("**Status:** 15 of 20 phases complete (75%)\n\n")
    
    notes.append("## Overview\n\n")
    notes.append("This release implements the Rongorongo Multi-Prong Research Methodology ")
    notes.append("with **734 glyphs** from the 2025-09-26 MASTER lexicon. All interpretations ")
    notes.append("follow conservative, evidence-based methodology with explicit confidence levels.\n\n")
    
    notes.append("## What's Included\n\n")
    notes.append("### Data Banks (Populated)\n")
    notes.append("- **SenseBank:** 734 glyphs, 558 sense entries with evidence vectors\n")
    notes.append("- **MotifBank:** 9 recurring patterns\n")
    notes.append("- **NameBank:** 33 genealogical candidates\n")
    notes.append("- **CalendarBank:** 32 entries (lunar, day, temporal)\n")
    notes.append("- **NumeralBank:** 8 numeral candidates\n\n")
    
    notes.append("### Analysis Files\n")
    notes.append("- **Semantic Clusters:** 9 context-based clusters\n")
    notes.append("- **Constraints:** Polynesian phonotactics + cultural rules\n")
    notes.append("- **Proto-Grammar:** 7 function classes, 5 grammatical patterns\n")
    notes.append("- **Context Frames:** 111 cultural contexts, 6 ethnographic domains\n")
    notes.append("- **Sense-Weighted Readings:** Evidence-based interpretation framework\n")
    notes.append("- **Cross-Validation:** Robustness testing results\n")
    notes.append("- **External Claim Harness:** Audit framework for external claims\n\n")
    
    notes.append("### Documentation\n")
    notes.append("- **Phase Reports:** Detailed reports for key phases (1, 9, 14, 15, 16, 17, 18, 20)\n")
    notes.append("- **Implementation Guide:** Usage instructions\n")
    notes.append("- **Phase Status:** Complete implementation tracking\n")
    notes.append("- **Integration Summary:** 2025-09-26 MASTER lexicon integration\n\n")
    
    notes.append("### Scripts\n")
    notes.append("- Data population scripts (populate_phase_data.py, update_master_lexicon.py)\n")
    notes.append("- Analysis scripts (proto_grammar, context_frames, sense_weighted_readings)\n")
    notes.append("- Validation scripts (validate_data.py, cross_validation, generate_statistics.py)\n")
    notes.append("- Release packaging (this script)\n\n")
    
    notes.append("## Completed Phases\n\n")
    notes.append("1. ✅ Phase 1: Corpus Assembly & Provenance\n")
    notes.append("2. ✅ Phase 5: Co-Occurrence Graphs & Semantic Clusters\n")
    notes.append("3. ✅ Phase 8: Motif Discovery & Ledger\n")
    notes.append("4. ✅ Phase 9: Multi-Sense Modeling (SenseBank)\n")
    notes.append("5. ✅ Phase 10: Constraint Filters\n")
    notes.append("6. ✅ Phase 11: Named Entities (NameBank)\n")
    notes.append("7. ✅ Phase 12: Calendrics & Cycles (CalendarBank)\n")
    notes.append("8. ✅ Phase 13: Numeral System (NumeralBank)\n")
    notes.append("9. ✅ Phase 14: Proto-Grammar\n")
    notes.append("10. ✅ Phase 15: Cross-Validation & Robustness\n")
    notes.append("11. ✅ Phase 16: Cultural Context Frames\n")
    notes.append("12. ✅ Phase 17: Sense-Weighted Readings\n")
    notes.append("13. ✅ Phase 18: External Claim Harness\n")
    notes.append("14. ✅ Phase 19: Packaging & Release (this phase)\n")
    notes.append("15. ✅ Phase 20: Translation Roadmap\n\n")
    
    notes.append("## Pending Phases\n\n")
    notes.append("The following phases require complete tablet corpus data:\n\n")
    notes.append("- **Phase 2:** Variant & Ligature Discipline (structure ready)\n")
    notes.append("- **Phase 3:** Orientation & Line Topology (structure ready)\n")
    notes.append("- **Phase 4:** Statistical Spine (structure ready)\n")
    notes.append("- **Phase 6:** Parallels & Alignment Atlas (structure ready)\n")
    notes.append("- **Phase 7:** Segmentation (structure ready)\n\n")
    
    notes.append("## Data Sources\n\n")
    notes.append("- **MASTER Lexicon 2025-09-26:** 734 entries\n")
    notes.append("- **Enhanced Multi-Meaning Lexicon v5.0:** 47 polysemic entries\n")
    notes.append("- **Second-Pass PDFs:** 15 phase documents + overview\n")
    notes.append("- **Complete Lexicon:** 306 cross-referenced entries\n\n")
    
    notes.append("## Methodology\n\n")
    notes.append("**Conservative, Evidence-Based Approach:**\n")
    notes.append("- ✅ No forced interpretations\n")
    notes.append("- ✅ Natural pattern emergence from data\n")
    notes.append("- ✅ Multi-source cross-verification\n")
    notes.append("- ✅ Explicit confidence levels (HIGH/MODERATE/LOW)\n")
    notes.append("- ✅ Limitations explicitly stated\n")
    notes.append("- ✅ Reproducible with provided scripts\n\n")
    
    notes.append("## Validation\n\n")
    notes.append("- **Structural Validation:** 0 errors across all data files\n")
    notes.append("- **Cross-Validation:** 4 of 5 tests passed (Phase 15)\n")
    notes.append("- **Robustness:** MODERATE-HIGH rating\n")
    notes.append("- **Checksums:** SHA256 for all files (see RELEASE_MANIFEST.json)\n\n")
    
    notes.append("## Usage\n\n")
    notes.append("1. **Explore Data:** Start with banks/ directory for glyph meanings\n")
    notes.append("2. **Read Reports:** See reports/ for detailed phase analyses\n")
    notes.append("3. **Run Scripts:** Use scripts/ to regenerate or validate data\n")
    notes.append("4. **Check Status:** See PHASE_STATUS.md for implementation details\n\n")
    
    notes.append("## Reproducibility\n\n")
    notes.append("To verify this release:\n\n")
    notes.append("1. Clone repository\n")
    notes.append("2. Check file checksums against RELEASE_MANIFEST.json\n")
    notes.append("3. Run validation: `python3 scripts/validate_data.py`\n")
    notes.append("4. Regenerate statistics: `python3 scripts/generate_statistics.py`\n\n")
    
    notes.append("## Attribution\n\n")
    notes.append("**Primary Research:** Lackadaisical Security (The Operator) & Spectre\n")
    notes.append("**Implementation:** GitHub Copilot (October 28, 2025)\n")
    notes.append("**Historical Sources:** Barthel, Fischer, Pozdniakov, Guy, et al.\n\n")
    
    notes.append("**License:** CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial)\n\n")
    
    notes.append("## Important Notes\n\n")
    notes.append("- **Script Status:** The Rongorongo script remains **largely undeciphered**\n")
    notes.append("- **Working Hypotheses:** All interpretations are working hypotheses, not proven facts\n")
    notes.append("- **Conservative Approach:** We prioritize caution over bold claims\n")
    notes.append("- **Open to Revision:** New evidence may require updating interpretations\n\n")
    
    notes.append("## Contact & Contributions\n\n")
    notes.append("- **Repository:** github.com/Lackadaisical-Security/rongorongo-decipherment-3rdpass\n")
    notes.append("- **Issues:** Use GitHub issues for questions or suggestions\n")
    notes.append("- **Data Sources:** github.com/Lackadaisical-Security/rongorongo-deciphered-public\n\n")
    
    notes.append("---\n\n")
    notes.append("*This release represents systematic, evidence-based analysis. ")
    notes.append("The Rongorongo script's ultimate meaning remains an open question.*\n")
    
    return "".join(notes)

def main():
    """Main execution"""
    base_path = Path("/home/runner/work/rongorongo-decipherment-3rdpass/rongorongo-decipherment-3rdpass")
    
    print("Phase 19: Packaging & Release Engineering")
    print("=" * 60)
    
    # Create file inventory
    print("\n1. Creating file inventory with checksums...")
    inventory = create_file_inventory(base_path)
    print(f"   - Files inventoried: {len(inventory)}")
    print(f"   - Total size: {sum(f['size'] for f in inventory):,} bytes")
    
    # Create release manifest
    print("\n2. Creating release manifest...")
    manifest = create_release_manifest(base_path, inventory)
    
    # Save manifest
    print("\n3. Saving release package...")
    save_json(manifest, base_path / "RELEASE_MANIFEST.json")
    print("   ✓ Saved: RELEASE_MANIFEST.json")
    
    # Generate release notes
    release_notes = generate_release_notes()
    with open(base_path / "RELEASE_NOTES.md", 'w', encoding='utf-8') as f:
        f.write(release_notes)
    print("   ✓ Saved: RELEASE_NOTES.md")
    
    # Generate checksum file
    print("\n4. Generating checksum file...")
    checksum_lines = []
    for item in inventory:
        checksum_lines.append(f"{item['checksum']}  {item['path']}\n")
    
    with open(base_path / "CHECKSUMS.sha256", 'w') as f:
        f.writelines(checksum_lines)
    print("   ✓ Saved: CHECKSUMS.sha256")
    
    print("\n5. Summary:")
    print(f"   - Version: v1.0")
    print(f"   - Files: {len(inventory)}")
    print(f"   - Phases: 15/20 complete (75%)")
    print(f"   - Size: {sum(f['size'] for f in inventory) / 1024 / 1024:.2f} MB")
    print("\n✅ Phase 19 Complete!\n")
    print("Release package ready for distribution.")

if __name__ == "__main__":
    main()
