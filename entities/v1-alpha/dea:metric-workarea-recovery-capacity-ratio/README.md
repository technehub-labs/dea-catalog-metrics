# dea:metric-workarea-recovery-capacity-ratio

Candidate Performance Metric record for **Workarea Recovery Capacity Ratio** (WRCR-BC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-workarea-recovery-capacity-ratio`
- **Name:** Workarea Recovery Capacity Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** WRCR-BC

## 2. Definition

Within Business Continuity & Disaster Recovery, Workarea Recovery Capacity Ratio (WRCR-BC) is used to gauge the utilization or availability of capacity. It is computed as Recovery Workstations Available / Required for Critical Teams, expressed in ratio (x:1 or x). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures whether alternate workspace capacity can absorb the staff required to run critical functions. Workforce recovery is the forgotten third of continuity after systems and sites. Capacity measured in seats without communications and equipment is half-ready. Read with alternate site readiness rate and continuity plan activation success rate.

## Formula

```
Recovery Workstations Available / Required for Critical Teams
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** risk
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_continuity_disaster_recovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3533 (batch 8)
