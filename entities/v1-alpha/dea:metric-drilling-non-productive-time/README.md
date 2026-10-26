# dea:metric-drilling-non-productive-time

Candidate Performance Metric record for **Drilling Non-Productive Time** (NPT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-drilling-non-productive-time`
- **Name:** Drilling Non-Productive Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NPT

## 2. Definition

A Oil & Gas indicator, Drilling Non-Productive Time (NPT) quantifies how efficiently resources are converted into outputs. The formula is Non-Productive Drilling Hours / Total Drilling Hours - reported in percent (%). It is a standard measure in the Oil & gas sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of rig time not drilling productively. It matters because NPT is pure cost at rig day rates among the highest in industry. NPT categories can be redefined so weather or waiting-on-orders time falls outside the metric. Read with Cost per Foot Drilled and rig operational efficiency to confirm NPT control is genuine.

## Formula

```
Non-Productive Drilling Hours / Total Drilling Hours
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** oil_gas
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 887 (batch 3)
