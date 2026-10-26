# dea:metric-cloud-cost-per-workload-unit

Candidate Performance Metric record for **Cloud Cost per Workload Unit** (CCPW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cloud-cost-per-workload-unit`
- **Name:** Cloud Cost per Workload Unit
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCPW

## 2. Definition

Within Data Centers & Cloud Infrastructure, Cloud Cost per Workload Unit (CCPW) is used to gauge how efficiently resources are converted into outputs. It is computed as Cloud Spend / Workload Units, expressed in currency per unit. Its use is concentrated in Technology. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Cloud Spend / Workload Units
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_centers_cloud_infrastructure
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2145 (batch 6)
