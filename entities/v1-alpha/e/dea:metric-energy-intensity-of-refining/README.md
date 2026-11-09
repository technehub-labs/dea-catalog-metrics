# dea:metric-energy-intensity-of-refining

Candidate Performance Metric record for **Energy Intensity of Refining** (EIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-energy-intensity-of-refining`
- **Name:** Energy Intensity of Refining
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EIR

## 2. Definition

A Oil & Gas indicator, Energy Intensity of Refining (EIR) quantifies how efficiently resources are converted into outputs. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Refinery Energy Consumed / Crude Throughput, expressed in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Oil & gas.

## 3. Context

Measures energy consumed per barrel or ton processed. It matters because refining margins hinge on energy cost and emissions compliance. Heavier crude slates can be hidden by normalizing to design crude, flattering the metric. Read with Gross Margin per Barrel and emissions intensity to confirm efficiency gains are real.

## Formula

```
EIR = Refinery Energy Consumed / Crude Throughput
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** oil_gas
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 884 (batch 3)
