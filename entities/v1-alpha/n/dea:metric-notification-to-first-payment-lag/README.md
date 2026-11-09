# dea:metric-notification-to-first-payment-lag

Candidate Performance Metric record for **Notification to First Payment Lag** (NFPL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-notification-to-first-payment-lag`
- **Name:** Notification to First Payment Lag
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NFPL

## 2. Definition

Notification to First Payment Lag (NFPL) captures how efficiently resources are converted into outputs for organizations tracking insurance claims deep dive. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Days from Claim Notification to First Payment; the result is stated in days. It should be driven down, since lower readings signal healthier performance. In Insurance, it is a recognized element of the standard performance toolkit.

## Formula

```
NFPL = Days from Claim Notification to First Payment
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1560 (batch 6)
