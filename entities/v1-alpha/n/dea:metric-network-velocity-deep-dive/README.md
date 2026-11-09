# dea:metric-network-velocity-deep-dive

Candidate Performance Metric record for **Network Velocity (Deep Dive)** (NVD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-network-velocity-deep-dive`
- **Name:** Network Velocity (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NVD

## 2. Definition

Network Velocity (Deep Dive) (NVD) addresses how efficiently resources are converted into outputs and is a fixture of rail freight (deep dive) reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Kilometres per Wagon Day; the result is stated in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. In Rail, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures average train speed across the network, including dwell. Velocity is the capacity alchemy of rail: faster networks carry more trains on the same track, and velocity improvements add capacity without capital - which is why velocity is the strategic metric of rail operations. Velocity gains from skipping cars (leaving freight behind) move congestion to terminals rather than solving it. Read with terminal dwell times and train load factor - tonnes per train (Deep Dive).

## Formula

```
NVD = Kilometres per Wagon Day
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_freight_deep_dive
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2422 (batch 6)
