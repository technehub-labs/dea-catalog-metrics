# dea:metric-time-to-value-onboarding-saas-deep-dive

Candidate Performance Metric record for **Time to Value - Onboarding (SaaS Deep Dive)** (TTV-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-value-onboarding-saas-deep-dive`
- **Name:** Time to Value - Onboarding (SaaS Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TTV-D

## 2. Definition

Time to Value - Onboarding (SaaS Deep Dive) (TTV-D) captures how efficiently resources are converted into outputs for organizations tracking software product operations (deep dive). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Days from Signup to First Value Milestone, expressed in days. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Technology.

## 3. Context

Measures elapsed time from contract signature to the customer achieving defined first-value outcomes. It is the activation gate for renewal economics: long onboarding is the strongest predictor of first-year churn, since customers pay while awaiting value. Definition integrity matters - login by the admin is not value, and stage-gated definitions must be pre-agreed. Read with activation rate (SaaS Deep Dive) and onboarding-effort drivers.

## Formula

```
Days from Signup to First Value Milestone
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** software_product_operations_deep_dive
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2155 (batch 6)
