# dea:metric-data-quality-cost-of-poor-quality

Candidate Performance Metric record for **Data Quality Cost of Poor Quality** (DQPQ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-quality-cost-of-poor-quality`
- **Name:** Data Quality Cost of Poor Quality
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DQPQ

## 2. Definition

Data Quality Cost of Poor Quality (DQPQ) addresses the economic value created or preserved and is a fixture of data quality management reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Estimated Rework and Error Cost per Quarter, expressed in currency value. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the financial cost of defective data: rework, bad decisions, compliance failures. Cost converts data quality from IT concern to P&L concern. Cost models built only on direct rework vastly understate decision-cost. Read with data quality trend index and data quality root cause closure rate.

## Formula

```
Estimated Rework and Error Cost per Quarter
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3630 (batch 8)
