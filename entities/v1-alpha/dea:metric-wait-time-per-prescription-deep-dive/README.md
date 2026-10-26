# dea:metric-wait-time-per-prescription-deep-dive

Candidate Performance Metric record for **Wait Time per Prescription (Deep Dive)** (WTP-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-wait-time-per-prescription-deep-dive`
- **Name:** Wait Time per Prescription (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WTP-D

## 2. Definition

Wait Time per Prescription (Deep Dive) (WTP-D) measures how efficiently resources are converted into outputs in the Pharmacy Retail domain. It is computed as Minutes from Drop-Off to Ready, expressed in minutes. Its use is concentrated in Healthcare. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
WTP-D = Minutes from Drop-Off to Ready
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2284 (batch 6)
