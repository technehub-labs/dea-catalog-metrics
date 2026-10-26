# dea:metric-capex-utilization-rate

Candidate Performance Metric record for **Capex Utilization Rate** (CUR-FP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-capex-utilization-rate`
- **Name:** Capex Utilization Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CUR-FP

## 2. Definition

Capex Utilization Rate (CUR-FP) captures the economic value created or preserved for organizations tracking financial planning & analysis. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Capex Spent vs Approved Plan / Plan, measured in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how much approved capital investment is actually deployed and delivering. Approved-but-stalled capex is strategy paused. Utilization measured at commitment rather than operation hides the stall. Read with capital allocation fulfilment rate and capital allocation effectiveness score.

## Formula

```
Capex Spent vs Approved Plan / Plan
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** financial_planning_analysis

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3787 (batch 8)
