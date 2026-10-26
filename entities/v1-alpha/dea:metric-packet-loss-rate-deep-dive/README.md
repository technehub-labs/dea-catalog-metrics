# dea:metric-packet-loss-rate-deep-dive

Candidate Performance Metric record for **Packet Loss Rate (Deep Dive)** (PLR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-packet-loss-rate-deep-dive`
- **Name:** Packet Loss Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PLR-D

## 2. Definition

Packet Loss Rate (Deep Dive) (PLR-D) addresses the quality of outputs and outcomes and is a fixture of telecom network operations (deep dive) reporting. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Lost Packets / Transmitted Packets, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Telecommunications.

## Formula

```
PLR-D = Lost Packets / Transmitted Packets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations_deep_dive
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2128 (batch 6)
