# dea:metric-transit-damage-claims-rate

Candidate Performance Metric record for **Transit Damage Claims Rate** (TDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-transit-damage-claims-rate`
- **Name:** Transit Damage Claims Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TDC

## 2. Definition

A Logistics & Transportation indicator, Transit Damage Claims Rate (TDC) quantifies the quality of outputs and outcomes. Its calculation is Claims Value / Freight Value Shipped, measured in percent (%). It originates from and is most used in Logistics practice. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures damage claims as a share of shipments or freight value. It matters because in-transit damage silently consumes margin and erodes customer trust. Gaming risk includes discouraging customers from filing claims or denying them via packaging blame-shifting. Read with Perfect Order Rate and Insurance/Claims recovery metrics to check damage is being reduced, not just reclassified.

## Formula

```
TDC = Claims Value / Freight Value Shipped
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** logistics_transportation
- **Sector:** logistics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 205 (batch 1)
