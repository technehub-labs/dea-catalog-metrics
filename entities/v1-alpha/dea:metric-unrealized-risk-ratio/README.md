# dea:metric-unrealized-risk-ratio

Candidate Performance Metric record for **Unrealized Risk Ratio** (URR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-unrealized-risk-ratio`
- **Name:** Unrealized Risk Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** URR-P

## 2. Definition

Unrealized Risk Ratio (URR-P) measures the quality of outputs and outcomes in the Project Risk & Issue Management domain. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Risks That Materialized but Were Not on Register / Materialized Risks - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Risks That Materialized but Were Not on Register / Materialized Risks
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** project_risk_issue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3426 (batch 7)
