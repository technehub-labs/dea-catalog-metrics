# dea:metric-insurance-rejection-rate-pharmacy

Candidate Performance Metric record for **Insurance Rejection Rate (Pharmacy)** (IRR-Ph) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-insurance-rejection-rate-pharmacy`
- **Name:** Insurance Rejection Rate (Pharmacy)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IRR-Ph

## 2. Definition

Insurance Rejection Rate (Pharmacy) (IRR-Ph) captures how efficiently resources are converted into outputs for organizations tracking pharmacy retail. Its calculation is Rejected Claims / Claims Submitted, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Healthcare practice.

## Formula

```
IRR-Ph = Rejected Claims / Claims Submitted
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** pharmacy_retail
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2289 (batch 6)
