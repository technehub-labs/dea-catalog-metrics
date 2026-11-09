# dea:metric-3-d-secure-pass-rate

Candidate Performance Metric record for **3-D Secure Pass Rate** (3DSP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-3-d-secure-pass-rate`
- **Name:** 3-D Secure Pass Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** 3DSP

## 2. Definition

A Payments & Cards (Deep Dive) indicator, 3-D Secure Pass Rate (3DSP) quantifies exposure to adverse outcomes. It is defined as 3DS Authenticated Successfully / 3DS Challenges; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. In Payments, it is a recognized element of the standard performance toolkit.

## Formula

```
3DSP = 3DS Authenticated Successfully / 3DS Challenges
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** payments_cards_deep_dive
- **Sector:** payments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2095 (batch 6)
