# dea:metric-loss-trend-estimation-error

Candidate Performance Metric record for **Loss Trend Estimation Error** (LTE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-loss-trend-estimation-error`
- **Name:** Loss Trend Estimation Error
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LTE

## 2. Definition

Loss Trend Estimation Error (LTE) captures the quality of outputs and outcomes for organizations tracking actuarial & reserving. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Actual Loss Trend - Estimated Loss Trend - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Insurance sector.

## 3. Context

Measures deviation between assumed loss trend (frequency, severity) and realized trend. Trend errors compound through every pricing and reserving projection, making this the upstream source of much downstream misstatement. Beware short-window trend fitting chasing recent noise, and social inflation effects that trend models persistently underweight. Read with rate adequacy index (Underwriting) and reserve development patterns for transmission of the error.

## Formula

```
Actual Loss Trend - Estimated Loss Trend
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** actuarial_reserving
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1535 (batch 6)
