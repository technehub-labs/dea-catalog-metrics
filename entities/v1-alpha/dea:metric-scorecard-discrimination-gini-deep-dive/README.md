# dea:metric-scorecard-discrimination-gini-deep-dive

Candidate Performance Metric record for **Scorecard Discrimination (Gini - Deep Dive)** (GINI-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-scorecard-discrimination-gini-deep-dive`
- **Name:** Scorecard Discrimination (Gini - Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GINI-D

## 2. Definition

A Banking Retail Lending (Deep Dive) indicator, Scorecard Discrimination (Gini - Deep Dive) (GINI-D) quantifies capability maturity or development. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Rank-Ordering Power of Credit Scorecard, expressed in index (0-100 or normalized). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Banking.

## 3. Context

Measures the rank-ordering power of credit scorecards - Gini (or AUC) on out-of-time data. Discrimination is the first-order quality test of a credit model, and it decays with population drift and macro cycles, so out-of-time validation matters more than in-sample elegance. High Gini with poor calibration still misprices, so pair discrimination with calibration measures. Read with approval-rate segments and early payment default - 3 Month for where the model fails.

## Formula

```
GINI-D = Rank-Ordering Power of Credit Scorecard
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** financial
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** banking_retail_lending_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2078 (batch 6)
