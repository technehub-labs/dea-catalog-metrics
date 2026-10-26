# dea:metric-monthly-member-churn

Candidate Performance Metric record for **Monthly Member Churn** (MMC-F) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-monthly-member-churn`
- **Name:** Monthly Member Churn
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MMC-F

## 2. Definition

Monthly Member Churn (MMC-F) measures exposure to adverse outcomes in the Fitness & Wellness domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Members Cancelling in Month / Members at Start, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Fitness & wellness practice.

## 3. Context

Monthly member churn measures the share of members leaving each month, and it is the fitness industry's unit-attrition metric that directly governs growth math - because member acquisition costs are real (marketing, sales, onboarding) and churn compounds monthly, a club adding 5 percent of members per month with 4 percent churning grows only on a sliver of its acquisition spend. Churn is seasonal (January joiners who quit by March are an industry archetype, the New Year's resolution cohort), so cohort-based analysis is the only honest view - joining-month cohorts show wildly different retention curves. Read with new-versus-tenured churn (new members churn at much higher rates, meaning onboarding quality is the lever), attendance correlation, and win-back rate which recovers some economics.

## Formula

```
Members Cancelling in Month / Members at Start
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** fitness_wellness
- **Sector:** fitness_wellness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1031 (batch 3)
