# dea:metric-early-payment-default-3-month

Candidate Performance Metric record for **Early Payment Default - 3 Month** (EPD3) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-early-payment-default-3-month`
- **Name:** Early Payment Default - 3 Month
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EPD3

## 2. Definition

Early Payment Default - 3 Month (EPD3) captures exposure to adverse outcomes for organizations tracking banking retail lending (deep dive). It is computed as Defaults within 3 Months / Disbursed Loans, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Banking.

## 3. Context

Measures defaults emerging within ninety days of origination. EPD isolates underwriting failures from portfolio seasoning: a loan that defaults this fast was misoriginated, not unlucky, and EPD clusters by vintage identify the specific cohorts. Sale-with-recourse agreements treat EPD differently, so contractual handling affects economics. Read with first payment default rate and scorecard discrimination (Gini - Deep Dive) for the model's blind spots.

## Formula

```
Defaults within 3 Months / Disbursed Loans
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** banking_retail_lending_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2076 (batch 6)
