# dea:metric-time-to-first-value-saas

Candidate Performance Metric record for **Time to First Value (SaaS)** (TTFV-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-first-value-saas`
- **Name:** Time to First Value (SaaS)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TTFV-S

## 2. Definition

Time to First Value (SaaS) (TTFV-S) captures how efficiently resources are converted into outputs for organizations tracking customer success (b2b saas). It is computed as Days from Contract Start to First Value Milestone, expressed in days. Its use is concentrated in Software & SaaS. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
TTFV-S = Days from Contract Start to First Value Milestone
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_success_b2b_saas
- **Sector:** software_saas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 586 (batch 2)
