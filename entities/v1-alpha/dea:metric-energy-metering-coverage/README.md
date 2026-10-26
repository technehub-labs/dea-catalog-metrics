# dea:metric-energy-metering-coverage

Candidate Performance Metric record for **Energy Metering Coverage** (EMC-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-energy-metering-coverage`
- **Name:** Energy Metering Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EMC-E

## 2. Definition

Within Operations Energy Management, Energy Metering Coverage (EMC-E) is used to gauge capability maturity or development. The formula is Major Loads Metered / Major Loads - reported in percent (%). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of consumption covered by metered measurement. It matters because unmetered consumption is invisible and unmanageable. Coverage can count broken meters as covered. Read with Data Completeness for energy data and Meter Failure Rate to confirm coverage reflects working measurement.

## Formula

```
EMC-E = Major Loads Metered / Major Loads
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** operations_energy_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1437 (batch 5)
