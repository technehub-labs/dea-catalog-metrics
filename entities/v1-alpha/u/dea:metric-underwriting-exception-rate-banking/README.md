# dea:metric-underwriting-exception-rate-banking

Candidate Performance Metric record for **Underwriting Exception Rate (Banking)** (UER-B) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-underwriting-exception-rate-banking`
- **Name:** Underwriting Exception Rate (Banking)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** UER-B

## 2. Definition

Underwriting Exception Rate (Banking) (UER-B) measures exposure to adverse outcomes in the Banking Retail Lending (Deep Dive) domain. It is defined as Approved Loans beyond Policy / Approved Loans; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. In Banking, it is a recognized element of the standard performance toolkit.

## Formula

```
UER-B = Approved Loans beyond Policy / Approved Loans
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** banking_retail_lending_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2085 (batch 6)
