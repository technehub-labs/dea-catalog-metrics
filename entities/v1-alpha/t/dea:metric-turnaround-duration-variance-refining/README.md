# dea:metric-turnaround-duration-variance-refining

Candidate Performance Metric record for **Turnaround Duration Variance (Refining)** (TDVR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-turnaround-duration-variance-refining`
- **Name:** Turnaround Duration Variance (Refining)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TDVR

## 2. Definition

A Oil & Gas Downstream & Refining indicator, Turnaround Duration Variance (Refining) (TDVR) quantifies how efficiently resources are converted into outputs. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Actual Turnaround Days - Planned / Planned; the result is stated in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. In Oil & Gas, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures actual versus planned duration of scheduled major maintenance events. Turnarounds are planned outages with planned economics: overrun days are lost full-margin production, and duration variance is the single biggest determinant of annual profit in turnaround years. Scope discipline during execution (avoiding discovered-work creep) is the controllable lever. Read with turnaround scope-change logs and post-turnaround reliability performance.

## Formula

```
TDVR = Actual Turnaround Days - Planned / Planned
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** oil_gas_downstream_refining
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2301 (batch 6)
