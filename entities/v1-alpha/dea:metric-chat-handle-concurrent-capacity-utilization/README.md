# dea:metric-chat-handle-concurrent-capacity-utilization

Candidate Performance Metric record for **Chat-Handle Concurrent Capacity Utilization** (CHCCU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-chat-handle-concurrent-capacity-utilization`
- **Name:** Chat-Handle Concurrent Capacity Utilization
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CHCCU

## 2. Definition

Within Contact Center Standard Measures (Deep Dive), Chat-Handle Concurrent Capacity Utilization (CHCCU) is used to gauge the utilization or availability of capacity. It is computed as Active Concurrent Chats / Agents x Target Concurrency, expressed in ratio (x:1 or x). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Active Concurrent Chats / Agents x Target Concurrency
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4331 (batch 10)
