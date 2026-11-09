# dea:metric-curtailment-rate

Candidate Performance Metric record for **Curtailment Rate** (CR-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-curtailment-rate`
- **Name:** Curtailment Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CR-E

## 2. Definition

A Energy Transition & Renewables indicator, Curtailment Rate (CR-E) quantifies the utilization or availability of capacity. It is computed as Generation Curtailed / Generation Available, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is concentrated in Renewable energy.

## 3. Context

Measures the share of available renewable generation not dispatched or grid-restricted. It matters because curtailment is generation built but unpaid, eroding project returns. Curtailment definitions can exclude self-imposed outages to shrink the rate. Read with Grid Balancing Cost and Capacity Factor for the asset to confirm reductions are structural.

## Formula

```
CR-E = Generation Curtailed / Generation Available
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_transition_renewables
- **Sector:** renewable_energy

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1105 (batch 4)
