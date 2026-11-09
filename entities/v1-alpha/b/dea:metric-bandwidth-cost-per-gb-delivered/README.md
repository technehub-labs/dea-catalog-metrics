# dea:metric-bandwidth-cost-per-gb-delivered

Candidate Performance Metric record for **Bandwidth Cost per GB Delivered** (BCGB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bandwidth-cost-per-gb-delivered`
- **Name:** Bandwidth Cost per GB Delivered
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BCGB

## 2. Definition

Within Network Performance & Capacity, Bandwidth Cost per GB Delivered (BCGB) is used to gauge how efficiently resources are converted into outputs. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Network Spend / GB Delivered, expressed in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
BCGB = Network Spend / GB Delivered
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3348 (batch 7)
