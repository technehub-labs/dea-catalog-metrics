# dea:metric-feature-usage-rate

Candidate Performance Metric record for **Feature Usage Rate** (FUR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-feature-usage-rate`
- **Name:** Feature Usage Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FUR

## 2. Definition

Within Software Engineering, Feature Usage Rate (FUR) is used to gauge the economic value created or preserved. Its calculation is Active Feature Users / Eligible Users, measured in percent (%). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of users or accounts actively using a released feature. It matters because unused features are sunk cost that also bloat and complicate the product. It can be gamed by counting single accidental activations as adoption. Read with Feature Adoption Curve depth (repeat usage) and Customer Health Score to distinguish trial from habit.

## Formula

```
Active Feature Users / Eligible Users
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 298 (batch 1)
