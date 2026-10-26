# dea:metric-missed-connection-rate

Candidate Performance Metric record for **Missed Connection Rate** (MCR-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-missed-connection-rate`
- **Name:** Missed Connection Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MCR-A

## 2. Definition

Missed Connection Rate (MCR-A) addresses the quality of outputs and outcomes and is a fixture of airline operations (deep dive) reporting. Its calculation is Passengers Missing Connections / Connecting Passengers, measured in percent (%). It originates from and is most used in Airlines practice. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
MCR-A = Passengers Missing Connections / Connecting Passengers
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2262 (batch 6)
