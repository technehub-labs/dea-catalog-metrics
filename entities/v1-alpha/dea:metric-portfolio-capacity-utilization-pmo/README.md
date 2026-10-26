# dea:metric-portfolio-capacity-utilization-pmo

Candidate Performance Metric record for **Portfolio Capacity Utilization (PMO)** (PCU-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-portfolio-capacity-utilization-pmo`
- **Name:** Portfolio Capacity Utilization (PMO)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PCU-P

## 2. Definition

Portfolio Capacity Utilization (PMO) (PCU-P) addresses the utilization or availability of capacity and is a fixture of pmo & portfolio governance reporting. The formula is Committed Demand / Available Delivery Capacity - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how fully delivery capacity is committed under PMO governance. Overcommitment is the root cause of systematic slippage. Utilization above roughly 90% leaves no room for the urgent and the failed. Read with portfolio capacity utilization and demand-to-delivery cycle time.

## Formula

```
Committed Demand / Available Delivery Capacity
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pmo_portfolio_governance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3414 (batch 7)
