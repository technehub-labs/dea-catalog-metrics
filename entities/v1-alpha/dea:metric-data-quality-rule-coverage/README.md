# dea:metric-data-quality-rule-coverage

Candidate Performance Metric record for **Data Quality Rule Coverage** (DQRULE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-quality-rule-coverage`
- **Name:** Data Quality Rule Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DQRULE

## 2. Definition

Data Quality Rule Coverage (DQRULE) measures conformance to standards, plans, or obligations in the Data Quality Management domain. Its calculation is Data Assets with Active Quality Rules / Data Assets, measured in percent (%). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Data Assets with Active Quality Rules / Data Assets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3623 (batch 8)
