# dea:metric-ai-ethics-review-coverage

Candidate Performance Metric record for **AI Ethics Review Coverage** (AIERC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ai-ethics-review-coverage`
- **Name:** AI Ethics Review Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AIERC

## 2. Definition

Within AI Governance & Model Risk Management, AI Ethics Review Coverage (AIERC) is used to gauge governance. It is defined as High-Impact Use Cases Reviewed by Ethics Board / High-Impact Cases; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of high-risk or sensitive AI use cases reviewed by an ethics review process before deployment. Ethics review is the pre-deployment control for harms that compliance frameworks miss (manipulation, dignity, societal effects), and coverage gaps cluster in exactly the ambiguous use cases that need review most. Review effectiveness - documented concerns and changed decisions, not checkbox approvals - is the real test. Read with review-outcome tracking and escalation of contested cases to governance bodies.

## Formula

```
AIERC = High-Impact Use Cases Reviewed by Ethics Board / High-Impact Cases
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** governance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ai_governance_model_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2509 (batch 7)
