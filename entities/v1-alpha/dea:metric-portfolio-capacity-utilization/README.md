# dea:metric-portfolio-capacity-utilization

Candidate Performance Metric record for **Portfolio Capacity Utilization** (PCU-PPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-portfolio-capacity-utilization`
- **Name:** Portfolio Capacity Utilization
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PCU-PPM

## 2. Definition

Portfolio Capacity Utilization (PCU-PPM) captures the utilization or availability of capacity for organizations tracking program & portfolio management. It is defined as Committed Resource Capacity / Total Capacity; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures how fully the delivery capacity is committed against available capacity. Chronic overcommitment (over 100%) guarantees portfolio-wide slippage and attrition. Utilization near 100% leaves no capacity for the inevitable urgent work. Read with demand-to-delivery cycle time and project portfolio health distribution.

## Formula

```
Committed Resource Capacity / Total Capacity
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** program_portfolio_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2965 (batch 7)
