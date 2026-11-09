# dea:metric-fraud-model-coverage

Candidate Performance Metric record for **Fraud Model Coverage** (FMC-EF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fraud-model-coverage`
- **Name:** Fraud Model Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FMC-EF

## 2. Definition

Fraud Model Coverage (FMC-EF) addresses exposure to adverse outcomes and is a fixture of enterprise fraud & financial crime management reporting. The formula is Transaction Channels Monitored by Fraud Models / Channels - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how completely the transaction and behavior landscape is scored by fraud models. Unmodeled flows are unmonitored flows. Coverage counted by transaction count rather than value can miss high-value low-volume exposure. Read with fraud model performance (precision/recall) and fraud detection rate (Enterprise).

## Formula

```
FMC-EF = Transaction Channels Monitored by Fraud Models / Channels
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** enterprise_fraud_financial_crime_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3768 (batch 8)
