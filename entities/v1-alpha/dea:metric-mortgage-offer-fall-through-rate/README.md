# dea:metric-mortgage-offer-fall-through-rate

Candidate Performance Metric record for **Mortgage Offer Fall-Through Rate** (MOFTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mortgage-offer-fall-through-rate`
- **Name:** Mortgage Offer Fall-Through Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MOFTR

## 2. Definition

Mortgage Offer Fall-Through Rate (MOFTR) measures exposure to adverse outcomes in the Banking Retail Lending (Deep Dive) domain. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Offers Not Proceeding to Completion / Offers, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Banking practice.

## Formula

```
Offers Not Proceeding to Completion / Offers
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** banking_retail_lending_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2086 (batch 6)
