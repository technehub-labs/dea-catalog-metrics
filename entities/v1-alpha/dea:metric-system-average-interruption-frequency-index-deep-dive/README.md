# dea:metric-system-average-interruption-frequency-index-deep-dive

Candidate Performance Metric record for **System Average Interruption Frequency Index (Deep Dive)** (SAIFI-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-system-average-interruption-frequency-index-deep-dive`
- **Name:** System Average Interruption Frequency Index (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SAIFI-D

## 2. Definition

System Average Interruption Frequency Index (Deep Dive) (SAIFI-D) captures the quality of outputs and outcomes for organizations tracking utilities field operations & grid. It is defined as Customer Interruptions / Customers Served; the result is stated in times per period. In Utilities, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

SAIFI, from IEEE Std 1366, is the average number of sustained interruptions per customer per year. It is the frequency companion to SAIDI: high SAIFI points to fault-prone feeders and exposure (overhead lines, vegetation, wildlife), while high SAIDI with low SAIFI points to slow restoration. Regulators increasingly set SAIFI targets in performance-based ratemaking, with rebates or penalties attached, so trend it both including and excluding major event days.

## Formula

```
SAIFI-D = Customer Interruptions / Customers Served
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** utilities_field_operations_grid
- **Sector:** utilities

## Attribution

- **Source credit:** IEEE Std 1366 reliability indices

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1883 (batch 6)
