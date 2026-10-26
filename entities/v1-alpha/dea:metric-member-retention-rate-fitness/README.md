# dea:metric-member-retention-rate-fitness

Candidate Performance Metric record for **Member Retention Rate (Fitness)** (MRR-F) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-member-retention-rate-fitness`
- **Name:** Member Retention Rate (Fitness)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MRR-F

## 2. Definition

A Fitness & Wellness indicator, Member Retention Rate (Fitness) (MRR-F) quantifies the retention of customers, users, or assets over time. Its calculation is Members Retained at Year End / Members at Start, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Fitness & wellness practice.

## 3. Context

Member retention rate measures the share of members staying over time, and it is the economics of the fitness business in one number - most gym models are membership businesses with prepaid commitments, so retaining members (even low-usage ones) is the entire margin game. The distinctive industry dynamic is the usage-retention link: members who attend at least a few times per month retain at multiples of the rate for members who never show up, making attendance the true leading indicator of churn. The dark-pattern incentive exists and must be named: gyms profit from non-attending members, so a business optimizing pure retention without engagement is monetizing failure. Read with monthly churn (its inverse), attendance frequency distribution, usage-based cohort retention curves, and contract-versus-monthly retention differences which reveal pricing model effects.

## Formula

```
Members Retained at Year End / Members at Start
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** fitness_wellness
- **Sector:** fitness_wellness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1030 (batch 3)
