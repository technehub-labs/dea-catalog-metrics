# dea:metric-scrap-cost-per-wafer

Candidate Performance Metric record for **Scrap Cost per Wafer** (SCW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-scrap-cost-per-wafer`
- **Name:** Scrap Cost per Wafer
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SCW

## 2. Definition

Scrap Cost per Wafer (SCW) captures how efficiently resources are converted into outputs for organizations tracking semiconductor & electronics. It is computed as Total Scrap Cost / Wafers Started, expressed in currency per unit. Its use is concentrated in Electronics & semiconductors. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures scrapped wafer cost per production unit. It matters because wafer value compounds through the process, so late-stage scrap is extremely expensive. Scrap definitions can exclude reworked or downgraded wafers. Read with Cycle Time Line Yield and Yield per Layer trends to confirm scrap reduction is genuine.

## Formula

```
Total Scrap Cost / Wafers Started
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** semiconductor_electronics
- **Sector:** electronics_semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 912 (batch 3)
