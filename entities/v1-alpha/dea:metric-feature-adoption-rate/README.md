# dea:metric-feature-adoption-rate

Candidate Performance Metric record for **Feature Adoption Rate** (FAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-feature-adoption-rate`
- **Name:** Feature Adoption Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FAR

## 2. Definition

Feature Adoption Rate (FAR) measures the economic value created or preserved in the Product Management domain. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Users Adopting New Feature / Users Exposed, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of target users adopting a released feature within a period. It matters because adoption is the only proof a shipped feature created value. Teams can define adoption as a single use, obscuring abandoned trials. Read with Feature Usage Rate and Net Revenue Retention contribution to confirm adoption is habitual and commercially meaningful.

## Formula

```
Users Adopting New Feature / Users Exposed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 554 (batch 1)
