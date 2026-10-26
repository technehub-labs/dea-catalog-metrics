# dea:metric-trunk-based-development-compliance

Candidate Performance Metric record for **Trunk-Based Development Compliance** (TBDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-trunk-based-development-compliance`
- **Name:** Trunk-Based Development Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TBDC

## 2. Definition

Trunk-Based Development Compliance (TBDC) captures conformance to standards, plans, or obligations for organizations tracking continuous integration. It is computed as Changes Merged to Trunk within 24 Hours / Changes, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Changes Merged to Trunk within 24 Hours / Changes
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_integration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2665 (batch 7)
