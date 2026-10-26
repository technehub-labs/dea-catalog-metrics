# dea:metric-vat-compliance-rate

Candidate Performance Metric record for **VAT Compliance Rate** (VATR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vat-compliance-rate`
- **Name:** VAT Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** VATR

## 2. Definition

VAT Compliance Rate (VATR) measures conformance to standards, plans, or obligations in the Tax & Fiscal domain. It is computed as VAT Returns and Payments On Time / VAT Periods, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
VATR = VAT Returns and Payments On Time / VAT Periods
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** tax_fiscal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 611 (batch 2)
