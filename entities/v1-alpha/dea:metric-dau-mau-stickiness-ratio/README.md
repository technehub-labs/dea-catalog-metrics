# dea:metric-dau-mau-stickiness-ratio

Candidate Performance Metric record for **DAU/MAU Stickiness Ratio** (DAUMAU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dau-mau-stickiness-ratio`
- **Name:** DAU/MAU Stickiness Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DAUMAU

## 2. Definition

DAU/MAU Stickiness Ratio (DAUMAU) measures the engagement or satisfaction of the people involved in the Web & Digital Analytics Standard Measures domain. Its calculation is Daily Active Users / Monthly Active Users, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Digital product practice.

## 3. Context

Measures daily active users as a share of monthly actives. Stickiness is the engagement signature that separates habitual products from occasional ones. Ratios compared across product categories mislead. Read with weekly retention cohort curve and session frequency per active user.

## Formula

```
Daily Active Users / Monthly Active Users
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** engagement
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** web_digital_analytics_standard_measures
- **Sector:** digital_product

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4358 (batch 11)
