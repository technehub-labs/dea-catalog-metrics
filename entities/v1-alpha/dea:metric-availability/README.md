# dea:metric-availability

Candidate Performance Metric record for **Availability** (AVL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-availability`
- **Name:** Availability
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AVL

## 2. Definition

Availability (AVL) measures the utilization or availability of capacity in the Maintenance & Reliability domain. The formula is Uptime / (Uptime + Downtime) - reported in percent (%). It is a standard measure in the Manufacturing sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of scheduled time an asset is capable of performing its function. It matters because equipment availability caps production capacity and delivery promises. Gaming risk includes keeping assets technically available while degraded, and recording waiting time as downtime vs available to taste. Read with Overall Equipment Effectiveness and Preventive Maintenance Compliance to confirm availability includes performance, not just presence.

## Formula

```
Uptime / (Uptime + Downtime)
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maintenance_reliability
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 269 (batch 1)
