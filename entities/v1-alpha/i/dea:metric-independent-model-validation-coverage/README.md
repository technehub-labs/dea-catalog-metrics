# dea:metric-independent-model-validation-coverage

Candidate Performance Metric record for **Independent Model Validation Coverage** (IMVC-AI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-independent-model-validation-coverage`
- **Name:** Independent Model Validation Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IMVC-AI

## 2. Definition

Within AI Governance & Model Risk Management, Independent Model Validation Coverage (IMVC-AI) is used to gauge exposure to adverse outcomes. It is computed as Material Models Independently Validated / Material Models, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of models receiving independent validation per policy. Independence is what makes validation credible: self-validation has the same conflict of interest as self-audit, and coverage gaps concentrate in exactly the models built fastest. Independence should be organizational, not just individual - validators reporting to model developers is structure theater. Read with validation findings-remediation closure and repeat-finding rates.

## Formula

```
IMVC-AI = Material Models Independently Validated / Material Models
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2491 (batch 7)
