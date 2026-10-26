# dea:metric-first-payment-default-rate

Candidate Performance Metric record for **First Payment Default Rate** (FPDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-first-payment-default-rate`
- **Name:** First Payment Default Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FPDR

## 2. Definition

A Banking Retail Lending (Deep Dive) indicator, First Payment Default Rate (FPDR) quantifies exposure to adverse outcomes. Its calculation is Borrowers Missing First Payment / Disbursed Loans, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. It originates from and is most used in Banking practice.

## 3. Context

Measures borrowers who never make a first payment after origination. First-payment defaults are the sharpest fraud and origination-quality signal in retail lending - genuine credit stress rarely appears before the borrower has paid once - and they implicate the underwriting or the channel. Track by origination source and channel, since misaligned incentive structures concentrate there. Read with early payment default - 3 Month and vintage loss curve accuracy.

## Formula

```
Borrowers Missing First Payment / Disbursed Loans
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2075 (batch 6)
