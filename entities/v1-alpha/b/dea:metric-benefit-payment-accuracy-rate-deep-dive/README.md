# dea:metric-benefit-payment-accuracy-rate-deep-dive

Candidate Performance Metric record for **Benefit Payment Accuracy Rate (Deep Dive)** (BPADD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-benefit-payment-accuracy-rate-deep-dive`
- **Name:** Benefit Payment Accuracy Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BPADD

## 2. Definition

Within Public Sector & Citizen Service Standard Measures (Deep Dive), Benefit Payment Accuracy Rate (Deep Dive) (BPADD) is used to gauge the quality of outputs and outcomes. Its calculation is Correct Payments / Payments Made, measured in percent (%). It originates from and is most used in Public sector practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of benefit payments at the correct amount to the correct eligible recipient. Payment accuracy is the fiduciary core of benefits administration. Accuracy measured on sampled cases with weak error-source analysis misses systematic defects. Read with improper payment rate and fraud detection rate (Enterprise).

## Formula

```
BPADD = Correct Payments / Payments Made
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** public_sector_citizen_service_standard_measures_deep_dive
- **Sector:** public_sector

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4419 (batch 11)
