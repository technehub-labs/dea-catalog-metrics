# dea:metric-onboarding-time-for-new-developer

Candidate Performance Metric record for **Onboarding Time for New Developer** (OTND) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-onboarding-time-for-new-developer`
- **Name:** Onboarding Time for New Developer
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OTND

## 2. Definition

Within Software Engineering, Onboarding Time for New Developer (OTND) is used to gauge capability maturity or development. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Days to First Meaningful Merged Contribution, measured in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how long a new developer takes to make their first meaningful, merged contribution. It matters because slow onboarding delays productivity in a scarce talent market. Teams can game it by counting trivial doc tweaks as the first contribution. Read with Developer Experience scores and First Week Commit milestones to confirm short onboarding is substantive.

## Formula

```
Days to First Meaningful Merged Contribution
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 297 (batch 1)
