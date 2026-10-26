# dea:metric-binding-authority-utilization

Candidate Performance Metric record for **Binding Authority Utilization** (BAU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-binding-authority-utilization`
- **Name:** Binding Authority Utilization
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BAU

## 2. Definition

Binding Authority Utilization (BAU) measures the utilization or availability of capacity in the Insurance Distribution & Agency Management domain. It is computed as Premium Bound under Delegated Authority / Authority Granted, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is concentrated in Insurance.

## Formula

```
Premium Bound under Delegated Authority / Authority Granted
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_agency_management
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1728 (batch 6)
