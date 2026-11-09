# dea:metric-s-op-forecast-consensus-rate

Candidate Performance Metric record for **S&OP Forecast Consensus Rate** (SFCSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-s-op-forecast-consensus-rate`
- **Name:** S&OP Forecast Consensus Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SFCSR

## 2. Definition

S&OP Forecast Consensus Rate (SFCSR) measures the engagement or satisfaction of the people involved in the Supply Chain Standard Measures (Deep Dive) domain. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Consensus Reached without Escalation / Planning Cycles, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
SFCSR = Consensus Reached without Escalation / Planning Cycles
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** engagement
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4268 (batch 10)
