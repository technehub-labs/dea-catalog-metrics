# dea:metric-connection-pool-saturation-rate

Candidate Performance Metric record for **Connection Pool Saturation Rate** (CPSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-connection-pool-saturation-rate`
- **Name:** Connection Pool Saturation Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CPSR

## 2. Definition

Connection Pool Saturation Rate (CPSR) addresses the utilization or availability of capacity and is a fixture of database & data platform operations reporting. It is defined as Peak Connections / Pool Capacity; the result is stated in percent (%). In Software, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
CPSR = Peak Connections / Pool Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** database_data_platform_operations
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3237 (batch 7)
