#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create External Claim Harness

Copyright © 2025 Lackadaisical Security
Website: https://lackadaisical-security.com
Support: support@lackadaisical-security.com
GitHub: https://github.com/Lackadaisical-Security/rongorongo-deciphered-public

Licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
https://creativecommons.org/licenses/by-nc/4.0/

Phase 18: External Claim Harness (Deferred Audits)

Creates framework for evaluating external claims about Rongorongo.
Establishes transparent audit methodology.

Methodology: Conservative, evidence-based, non-adversarial

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
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

def save_json(data: Any, filepath: Path):
    """Save JSON file with formatting"""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def create_audit_framework() -> Dict:
    """Create the audit evaluation framework"""
    return {
        "metadata": {
            "phase": "18 - External Claim Harness",
            "description": "Framework for evaluating external Rongorongo interpretations",
            "methodology": "Evidence-based, non-adversarial, transparent scoring",
            "purpose": "Systematic comparison without predetermined conclusions",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        "evaluation_criteria": {
            "evidence_quality": {
                "weight": 0.30,
                "description": "Quality and verifiability of evidence cited",
                "scoring": {
                    "3": "Primary sources, reproducible data, clear provenance",
                    "2": "Secondary sources, partial documentation",
                    "1": "Tertiary sources, limited documentation",
                    "0": "No sources cited or unverifiable claims"
                }
            },
            "cross_verification": {
                "weight": 0.25,
                "description": "Claims verified across multiple tablets/sources",
                "scoring": {
                    "3": "Verified across 3+ independent tablets",
                    "2": "Verified across 2 tablets",
                    "1": "Single tablet evidence",
                    "0": "No cross-tablet verification"
                }
            },
            "linguistic_plausibility": {
                "weight": 0.20,
                "description": "Consistency with known Polynesian linguistics",
                "scoring": {
                    "3": "Fully consistent with Rapanui/Polynesian patterns",
                    "2": "Mostly consistent, some exceptions explained",
                    "1": "Partially consistent, significant exceptions",
                    "0": "Inconsistent with established patterns"
                }
            },
            "falsifiability": {
                "weight": 0.15,
                "description": "Claim structured to allow testing/refutation",
                "scoring": {
                    "3": "Specific, testable predictions provided",
                    "2": "Some testable elements",
                    "1": "Limited testability",
                    "0": "Unfalsifiable or circular reasoning"
                }
            },
            "transparency": {
                "weight": 0.10,
                "description": "Openness about methods, limitations, uncertainties",
                "scoring": {
                    "3": "Full methodology disclosed, limitations acknowledged",
                    "2": "Partial methodology, some limitations noted",
                    "1": "Limited methodological disclosure",
                    "0": "Methodology hidden or unclear"
                }
            }
        },
        "scoring_guidelines": {
            "range": "0.0 - 3.0 (weighted average)",
            "interpretation": {
                "2.5-3.0": "Strong - Well-supported, verifiable claims",
                "2.0-2.4": "Good - Solid evidence with minor gaps",
                "1.5-1.9": "Moderate - Some evidence, needs strengthening",
                "1.0-1.4": "Weak - Limited evidence or methodology issues",
                "0.0-0.9": "Very Weak - Insufficient evidence or major issues"
            },
            "important_note": "Score reflects claim quality, not claim truth. High scores indicate well-constructed arguments deserving serious consideration."
        },
        "audit_types": [
            {
                "type": "Sign Assignment Audit",
                "description": "Evaluates proposed meaning assignments for individual glyphs",
                "key_questions": [
                    "What evidence supports this assignment?",
                    "Does it appear consistently across tablets?",
                    "Is it linguistically plausible?",
                    "Are alternative readings considered?"
                ]
            },
            {
                "type": "Sequence Interpretation Audit",
                "description": "Evaluates proposed readings of glyph sequences",
                "key_questions": [
                    "Is the grammatical structure justified?",
                    "Do parallel passages support this reading?",
                    "Are function words vs content words distinguished?",
                    "Is the translation culturally plausible?"
                ]
            },
            {
                "type": "System-Level Claim Audit",
                "description": "Evaluates broader claims about script nature or function",
                "key_questions": [
                    "Does claim account for all known tablets?",
                    "Is internal consistency maintained?",
                    "Are counter-examples addressed?",
                    "How does it compare to scholarly consensus?"
                ]
            }
        ]
    }

def create_sample_audits() -> List[Dict]:
    """Create sample audit templates"""
    return [
        {
            "claim_id": "SAMPLE-001",
            "claim_type": "Sign Assignment Audit",
            "claim_summary": "[Template for future audits]",
            "source": {
                "author": "[To be filled]",
                "publication": "[To be filled]",
                "year": None,
                "accessibility": "public/restricted"
            },
            "evaluation": {
                "evidence_quality": {"score": None, "notes": ""},
                "cross_verification": {"score": None, "notes": ""},
                "linguistic_plausibility": {"score": None, "notes": ""},
                "falsifiability": {"score": None, "notes": ""},
                "transparency": {"score": None, "notes": ""}
            },
            "overall_score": None,
            "assessment": "To be completed",
            "reviewer": "TBD",
            "review_date": None,
            "notes": "This is a template for conducting future audits"
        }
    ]

def generate_audit_report() -> str:
    """Generate markdown audit framework documentation"""
    report = []
    report.append("# Phase 18: External Claim Harness - Audit Framework\n\n")
    report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
    report.append("**Purpose:** Transparent evaluation of external Rongorongo claims\n\n")
    
    report.append("## Overview\n\n")
    report.append("This framework provides a **non-adversarial, evidence-based system** for evaluating ")
    report.append("external claims about Rongorongo interpretation. The goal is not to \"debunk\" ")
    report.append("but to systematically assess claim quality and identify areas for productive dialogue.\n\n")
    
    report.append("## Guiding Principles\n\n")
    report.append("1. **Non-Adversarial:** Approach all claims with intellectual curiosity\n")
    report.append("2. **Evidence-Based:** Focus on verifiable evidence, not authority\n")
    report.append("3. **Transparent:** Clear criteria, reproducible scoring\n")
    report.append("4. **Charitable:** Interpret claims in their strongest form\n")
    report.append("5. **Humble:** Acknowledge our own limitations and uncertainties\n\n")
    
    report.append("## Evaluation Criteria\n\n")
    report.append("Claims are evaluated across 5 weighted dimensions:\n\n")
    
    report.append("### 1. Evidence Quality (30%)\n\n")
    report.append("- **3 points:** Primary sources, reproducible data, clear provenance\n")
    report.append("- **2 points:** Secondary sources, partial documentation\n")
    report.append("- **1 point:** Tertiary sources, limited documentation\n")
    report.append("- **0 points:** No sources cited or unverifiable claims\n\n")
    
    report.append("### 2. Cross-Verification (25%)\n\n")
    report.append("- **3 points:** Verified across 3+ independent tablets\n")
    report.append("- **2 points:** Verified across 2 tablets\n")
    report.append("- **1 point:** Single tablet evidence\n")
    report.append("- **0 points:** No cross-tablet verification\n\n")
    
    report.append("### 3. Linguistic Plausibility (20%)\n\n")
    report.append("- **3 points:** Fully consistent with Rapanui/Polynesian patterns\n")
    report.append("- **2 points:** Mostly consistent, exceptions explained\n")
    report.append("- **1 point:** Partially consistent, significant exceptions\n")
    report.append("- **0 points:** Inconsistent with established patterns\n\n")
    
    report.append("### 4. Falsifiability (15%)\n\n")
    report.append("- **3 points:** Specific, testable predictions provided\n")
    report.append("- **2 points:** Some testable elements\n")
    report.append("- **1 point:** Limited testability\n")
    report.append("- **0 points:** Unfalsifiable or circular reasoning\n\n")
    
    report.append("### 5. Transparency (10%)\n\n")
    report.append("- **3 points:** Full methodology disclosed, limitations acknowledged\n")
    report.append("- **2 points:** Partial methodology, some limitations noted\n")
    report.append("- **1 point:** Limited methodological disclosure\n")
    report.append("- **0 points:** Methodology hidden or unclear\n\n")
    
    report.append("## Scoring Interpretation\n\n")
    report.append("**Final Score = Weighted Average (0.0 - 3.0)**\n\n")
    report.append("- **2.5-3.0:** Strong - Well-supported, verifiable claims\n")
    report.append("- **2.0-2.4:** Good - Solid evidence with minor gaps\n")
    report.append("- **1.5-1.9:** Moderate - Some evidence, needs strengthening\n")
    report.append("- **1.0-1.4:** Weak - Limited evidence or methodology issues\n")
    report.append("- **0.0-0.9:** Very Weak - Insufficient evidence or major issues\n\n")
    
    report.append("**Important:** A high score indicates a **well-constructed argument**, not necessarily ")
    report.append("a true claim. It signals the claim deserves serious scholarly consideration.\n\n")
    
    report.append("## Audit Types\n\n")
    report.append("### A. Sign Assignment Audit\n")
    report.append("Evaluates proposed glyph meanings\n\n")
    report.append("**Key Questions:**\n")
    report.append("- What evidence supports this assignment?\n")
    report.append("- Does it appear consistently across tablets?\n")
    report.append("- Is it linguistically plausible?\n")
    report.append("- Are alternative readings considered?\n\n")
    
    report.append("### B. Sequence Interpretation Audit\n")
    report.append("Evaluates proposed readings of glyph sequences\n\n")
    report.append("**Key Questions:**\n")
    report.append("- Is the grammatical structure justified?\n")
    report.append("- Do parallel passages support this reading?\n")
    report.append("- Are function words vs content words distinguished?\n")
    report.append("- Is the translation culturally plausible?\n\n")
    
    report.append("### C. System-Level Claim Audit\n")
    report.append("Evaluates broader claims about script nature/function\n\n")
    report.append("**Key Questions:**\n")
    report.append("- Does claim account for all known tablets?\n")
    report.append("- Is internal consistency maintained?\n")
    report.append("- Are counter-examples addressed?\n")
    report.append("- How does it compare to scholarly consensus?\n\n")
    
    report.append("## Using This Framework\n\n")
    report.append("1. **Select a Claim:** Choose specific external claim to evaluate\n")
    report.append("2. **Gather Evidence:** Collect all cited sources and supporting data\n")
    report.append("3. **Score Each Criterion:** Use scoring rubric for each dimension\n")
    report.append("4. **Calculate Weighted Average:** Apply weights to get final score\n")
    report.append("5. **Write Assessment:** Provide narrative summary and recommendations\n")
    report.append("6. **Store in Repository:** Save audit to `reports/claims/` directory\n\n")
    
    report.append("## Example Audit Structure\n\n")
    report.append("```json\n")
    report.append("{\n")
    report.append('  "claim_id": "AUDIT-001",\n')
    report.append('  "claim_type": "Sign Assignment Audit",\n')
    report.append('  "claim_summary": "Glyph B001 represents \'tangata\' (person)",\n')
    report.append('  "source": {\n')
    report.append('    "author": "Researcher Name",\n')
    report.append('    "publication": "Journal/Book",\n')
    report.append('    "year": 2024\n')
    report.append('  },\n')
    report.append('  "evaluation": {\n')
    report.append('    "evidence_quality": {"score": 3, "notes": "Multiple tablet attestations"},\n')
    report.append('    "cross_verification": {"score": 3, "notes": "Found on 5+ tablets"},\n')
    report.append('    "linguistic_plausibility": {"score": 3, "notes": "Consistent with Rapanui"},\n')
    report.append('    "falsifiability": {"score": 2, "notes": "Testable against new tablets"},\n')
    report.append('    "transparency": {"score": 3, "notes": "Full methodology disclosed"}\n')
    report.append('  },\n')
    report.append('  "overall_score": 2.9,\n')
    report.append('  "assessment": "Strong"\n')
    report.append("}\n")
    report.append("```\n\n")
    
    report.append("## Limitations\n\n")
    report.append("- **Subjective Elements:** Scoring involves judgment calls\n")
    report.append("- **Incomplete Information:** May not have access to all sources\n")
    report.append("- **Evolving Evidence:** New discoveries may change assessments\n")
    report.append("- **Not Final Judgment:** Audits are working assessments, not verdicts\n\n")
    
    report.append("## Future Work\n\n")
    report.append("1. Conduct audits of major published claims\n")
    report.append("2. Invite external reviewers for inter-rater reliability\n")
    report.append("3. Refine criteria based on experience\n")
    report.append("4. Publish results for scholarly dialogue\n\n")
    
    report.append("---\n\n")
    report.append("*This framework is a tool for productive scholarly discourse, ")
    report.append("not a weapon for dismissing alternative views. The Rongorongo script ")
    report.append("remains largely undeciphered, and all interpretations should be evaluated ")
    report.append("with intellectual humility and openness.*\n")
    
    return "".join(report)

def main():
    """Main execution"""
    base_path = Path("/home/runner/work/rongorongo-decipherment-3rdpass/rongorongo-decipherment-3rdpass")
    
    print("Phase 18: External Claim Harness (Audit Framework)")
    print("=" * 60)
    
    # Create framework
    print("\n1. Creating audit framework...")
    framework = create_audit_framework()
    
    # Create sample audits
    print("\n2. Creating sample audit templates...")
    sample_audits = create_sample_audits()
    
    # Save framework JSON
    print("\n3. Saving outputs...")
    output_data = {
        **framework,
        "sample_audits": sample_audits,
        "audit_directory": "reports/claims/",
        "usage_notes": "Use this framework to evaluate external Rongorongo claims systematically"
    }
    
    save_json(output_data, base_path / "analysis" / "external_claim_harness.json")
    print("   ✓ Saved: analysis/external_claim_harness.json")
    
    # Generate markdown report
    report_md = generate_audit_report()
    report_path = base_path / "reports" / "phase_18_external_claim_harness.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_md)
    print("   ✓ Saved: reports/phase_18_external_claim_harness.md")
    
    # Create claims directory
    claims_dir = base_path / "reports" / "claims"
    claims_dir.mkdir(parents=True, exist_ok=True)
    
    # Create README for claims directory
    readme_content = """# External Claim Audits

This directory contains audits of external Rongorongo interpretation claims.

## Purpose

Systematic evaluation of published interpretations using transparent, evidence-based criteria.

## Framework

See `reports/phase_18_external_claim_harness.md` for complete evaluation framework.

## Audit Files

Each audit should be named: `AUDIT-XXX_[brief-description].json`

Example: `AUDIT-001_glyph-B001-tangata.json`

## Adding Audits

1. Copy template from `analysis/external_claim_harness.json`
2. Fill in all fields
3. Calculate weighted score
4. Save to this directory
"""
    
    with open(claims_dir / "README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("   ✓ Created: reports/claims/README.md")
    
    print("\n4. Summary:")
    print("   - Audit framework created")
    print("   - 5 evaluation criteria defined")
    print("   - 3 audit types specified")
    print("   - Sample templates provided")
    print("\n✅ Phase 18 Complete!\n")

if __name__ == "__main__":
    main()
