# dea:metric-data-debt-backlog-age

Candidate Performance Metric record for **Data Debt Backlog Age** (DDBA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-debt-backlog-age`
- **Name:** Data Debt Backlog Age
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DDBA

## 2. Definition

Data Debt Backlog Age (DDBA) captures how efficiently resources are converted into outputs for organizations tracking data governance & stewardship. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Average Age of Open Data Governance Backlog Items, measured in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Average Age of Open Data Governance Backlog Items
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_governance_stewardship

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3614 (batch 8)
