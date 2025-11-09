# Phase 18: External Claim Harness - Audit Framework

**Generated:** 2025-10-28 23:12:42 UTC
**Purpose:** Transparent evaluation of external Rongorongo claims

## Overview

This framework provides a **non-adversarial, evidence-based system** for evaluating external claims about Rongorongo interpretation. The goal is not to "debunk" but to systematically assess claim quality and identify areas for productive dialogue.

## Guiding Principles

1. **Non-Adversarial:** Approach all claims with intellectual curiosity
2. **Evidence-Based:** Focus on verifiable evidence, not authority
3. **Transparent:** Clear criteria, reproducible scoring
4. **Charitable:** Interpret claims in their strongest form
5. **Humble:** Acknowledge our own limitations and uncertainties

## Evaluation Criteria

Claims are evaluated across 5 weighted dimensions:

### 1. Evidence Quality (30%)

- **3 points:** Primary sources, reproducible data, clear provenance
- **2 points:** Secondary sources, partial documentation
- **1 point:** Tertiary sources, limited documentation
- **0 points:** No sources cited or unverifiable claims

### 2. Cross-Verification (25%)

- **3 points:** Verified across 3+ independent tablets
- **2 points:** Verified across 2 tablets
- **1 point:** Single tablet evidence
- **0 points:** No cross-tablet verification

### 3. Linguistic Plausibility (20%)

- **3 points:** Fully consistent with Rapanui/Polynesian patterns
- **2 points:** Mostly consistent, exceptions explained
- **1 point:** Partially consistent, significant exceptions
- **0 points:** Inconsistent with established patterns

### 4. Falsifiability (15%)

- **3 points:** Specific, testable predictions provided
- **2 points:** Some testable elements
- **1 point:** Limited testability
- **0 points:** Unfalsifiable or circular reasoning

### 5. Transparency (10%)

- **3 points:** Full methodology disclosed, limitations acknowledged
- **2 points:** Partial methodology, some limitations noted
- **1 point:** Limited methodological disclosure
- **0 points:** Methodology hidden or unclear

## Scoring Interpretation

**Final Score = Weighted Average (0.0 - 3.0)**

- **2.5-3.0:** Strong - Well-supported, verifiable claims
- **2.0-2.4:** Good - Solid evidence with minor gaps
- **1.5-1.9:** Moderate - Some evidence, needs strengthening
- **1.0-1.4:** Weak - Limited evidence or methodology issues
- **0.0-0.9:** Very Weak - Insufficient evidence or major issues

**Important:** A high score indicates a **well-constructed argument**, not necessarily a true claim. It signals the claim deserves serious scholarly consideration.

## Audit Types

### A. Sign Assignment Audit
Evaluates proposed glyph meanings

**Key Questions:**
- What evidence supports this assignment?
- Does it appear consistently across tablets?
- Is it linguistically plausible?
- Are alternative readings considered?

### B. Sequence Interpretation Audit
Evaluates proposed readings of glyph sequences

**Key Questions:**
- Is the grammatical structure justified?
- Do parallel passages support this reading?
- Are function words vs content words distinguished?
- Is the translation culturally plausible?

### C. System-Level Claim Audit
Evaluates broader claims about script nature/function

**Key Questions:**
- Does claim account for all known tablets?
- Is internal consistency maintained?
- Are counter-examples addressed?
- How does it compare to scholarly consensus?

## Using This Framework

1. **Select a Claim:** Choose specific external claim to evaluate
2. **Gather Evidence:** Collect all cited sources and supporting data
3. **Score Each Criterion:** Use scoring rubric for each dimension
4. **Calculate Weighted Average:** Apply weights to get final score
5. **Write Assessment:** Provide narrative summary and recommendations
6. **Store in Repository:** Save audit to `reports/claims/` directory

## Example Audit Structure

```json
{
  "claim_id": "AUDIT-001",
  "claim_type": "Sign Assignment Audit",
  "claim_summary": "Glyph B001 represents 'tangata' (person)",
  "source": {
    "author": "Researcher Name",
    "publication": "Journal/Book",
    "year": 2024
  },
  "evaluation": {
    "evidence_quality": {"score": 3, "notes": "Multiple tablet attestations"},
    "cross_verification": {"score": 3, "notes": "Found on 5+ tablets"},
    "linguistic_plausibility": {"score": 3, "notes": "Consistent with Rapanui"},
    "falsifiability": {"score": 2, "notes": "Testable against new tablets"},
    "transparency": {"score": 3, "notes": "Full methodology disclosed"}
  },
  "overall_score": 2.9,
  "assessment": "Strong"
}
```

## Limitations

- **Subjective Elements:** Scoring involves judgment calls
- **Incomplete Information:** May not have access to all sources
- **Evolving Evidence:** New discoveries may change assessments
- **Not Final Judgment:** Audits are working assessments, not verdicts

## Future Work

1. Conduct audits of major published claims
2. Invite external reviewers for inter-rater reliability
3. Refine criteria based on experience
4. Publish results for scholarly dialogue

---

*This framework is a tool for productive scholarly discourse, not a weapon for dismissing alternative views. The Rongorongo script remains largely undeciphered, and all interpretations should be evaluated with intellectual humility and openness.*
