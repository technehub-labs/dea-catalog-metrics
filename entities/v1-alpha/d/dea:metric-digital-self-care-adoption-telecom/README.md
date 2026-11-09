# dea:metric-digital-self-care-adoption-telecom

Candidate Performance Metric record for **Digital Self-Care Adoption (Telecom)** (DSCA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-digital-self-care-adoption-telecom`
- **Name:** Digital Self-Care Adoption (Telecom)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DSCA

## 2. Definition

Digital Self-Care Adoption (Telecom) (DSCA) measures how efficiently resources are converted into outputs in the Telecom Customer Experience & Billing domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Digital Channel Resolutions / Total Resolutions; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Telecommunications, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of customer service transactions completed in app or web self-service without human contact. It matters because each migrated interaction removes several dollars of cost and, when done well, improves convenience perception simultaneously. Watch the dark side: adoption driven by degraded assisted service creates deflection, not satisfaction, and shows up later as churn. Exclude trivial automated notifications, or the number becomes meaningless. Read with cost per contact by channel and complaint rates from self-service users.

## Formula

```
DSCA = Digital Channel Resolutions / Total Resolutions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** telecom_customer_experience_billing
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1272 (batch 5)
