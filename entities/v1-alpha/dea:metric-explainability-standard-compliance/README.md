# dea:metric-explainability-standard-compliance

Candidate Performance Metric record for **Explainability Standard Compliance** (EXSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-explainability-standard-compliance`
- **Name:** Explainability Standard Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EXSC

## 2. Definition

Explainability Standard Compliance (EXSC) captures conformance to standards, plans, or obligations for organizations tracking ai governance & model risk management. Its calculation is Models Meeting Explainability Requirement / In-Scope Models, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether models used in consequential decisions meet the enterprise explainability standard (reason codes, feature importance, documentation). Explainability is the operational bridge between model performance and regulatory, ethical, and customer-communication requirements, and it is harder for complex models by design. Compliance must be tested at the decision level (can this specific denial be explained), not the model level. Read with adverse-action notice quality and complaint root causes about unexplained decisions.

## Formula

```
Models Meeting Explainability Requirement / In-Scope Models
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2501 (batch 7)
