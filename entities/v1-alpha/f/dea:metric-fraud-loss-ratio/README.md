# dea:metric-fraud-loss-ratio

Candidate Performance Metric record for **Fraud Loss Ratio** (FLR-EF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fraud-loss-ratio`
- **Name:** Fraud Loss Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FLR-EF

## 2. Definition

Fraud Loss Ratio (FLR-EF) captures exposure to adverse outcomes for organizations tracking enterprise fraud & financial crime management. It is computed as Fraud Losses / Revenue, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures fraud losses as a share of revenue or transaction volume. It is the headline scoreboard of the fraud program. Falling ratios can reflect under-detection rather than improvement. Read with fraud detection rate (Enterprise) and recovery rate (Fraud Losses).

## Formula

```
FLR-EF = Fraud Losses / Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** enterprise_fraud_financial_crime_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3755 (batch 8)
