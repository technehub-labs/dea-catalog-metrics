# dea:metric-decision-latency-under-risk

Candidate Performance Metric record for **Decision Latency under Risk** (DLUR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-decision-latency-under-risk`
- **Name:** Decision Latency under Risk
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DLUR

## 2. Definition

Decision Latency under Risk (DLUR) measures how efficiently resources are converted into outputs in the Project Risk & Issue Management domain. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Days Risk-Aged Decisions Pending, measured in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Days Risk-Aged Decisions Pending
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** risk
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3435 (batch 7)
