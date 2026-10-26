# dea:metric-packet-loss-rate-network-deep-dive

Candidate Performance Metric record for **Packet Loss Rate (Network Deep Dive)** (PLR-NW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-packet-loss-rate-network-deep-dive`
- **Name:** Packet Loss Rate (Network Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PLR-NW

## 2. Definition

Packet Loss Rate (Network Deep Dive) (PLR-NW) captures the quality of outputs and outcomes for organizations tracking network performance & capacity. It is a working-level control: thresholds trigger immediate operational response. It is defined as Packets Lost / Packets Sent; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
PLR-NW = Packets Lost / Packets Sent
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3344 (batch 7)
