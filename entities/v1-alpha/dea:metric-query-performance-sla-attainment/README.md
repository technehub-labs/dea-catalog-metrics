# dea:metric-query-performance-sla-attainment

Candidate Performance Metric record for **Query Performance SLA Attainment** (QPSLAA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-query-performance-sla-attainment`
- **Name:** Query Performance SLA Attainment
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** QPSLAA

## 2. Definition

Query Performance SLA Attainment (QPSLAA) captures the quality of outputs and outcomes for organizations tracking data science & analytics operations. The formula is Dashboards Meeting Query Latency SLA / Dashboards - reported in percent (%). It is applied across virtually every sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
QPSLAA = Dashboards Meeting Query Latency SLA / Dashboards
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_science_analytics_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2594 (batch 7)
