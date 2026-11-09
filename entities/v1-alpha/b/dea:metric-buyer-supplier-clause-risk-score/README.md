# dea:metric-buyer-supplier-clause-risk-score

Candidate Performance Metric record for **Buyer-Supplier Clause Risk Score** (BSCRS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-buyer-supplier-clause-risk-score`
- **Name:** Buyer-Supplier Clause Risk Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BSCRS

## 2. Definition

Within Contract Lifecycle Management, Buyer-Supplier Clause Risk Score (BSCRS) is used to gauge exposure to adverse outcomes. It is defined as Average Risk Balance Score of Executed Terms; the result is stated in score (points). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures aggregate risk profile of accepted clause terms across the contract estate. Clause positions compound: each accepted risk term accumulates exposure. Scores from templates rather than executed contracts measure intent, not reality. Read with contract compliance rate and third-party contract risk assessment.

## Formula

```
BSCRS = Average Risk Balance Score of Executed Terms
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contract_lifecycle_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3710 (batch 8)
