# dea:metric-port-berth-productivity-moves-per-hour-deep-dive

Candidate Performance Metric record for **Port Berth Productivity - Moves per Hour (Deep Dive)** (PBPH-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-port-berth-productivity-moves-per-hour-deep-dive`
- **Name:** Port Berth Productivity - Moves per Hour (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PBPH-D

## 2. Definition

Port Berth Productivity - Moves per Hour (Deep Dive) (PBPH-D) measures how efficiently resources are converted into outputs in the Maritime Shipping (Deep Dive) domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Container Moves / Berth Hour - reported in count (items per period). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Maritime sector.

## 3. Context

Measures container moves per vessel hour at berth. It is the capacity metric of port economics: berth time is the scarce resource ships and terminals trade on, and productivity determines port competitiveness, vessel schedule integrity, and terminal profitability. Ship size drives raw productivity (bigger ships move more per hour), so normalize for vessel class. Read with yard and gate productivity - berth gains bottleneck one node inland.

## Formula

```
PBPH-D = Container Moves / Berth Hour
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping_deep_dive
- **Sector:** maritime

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2431 (batch 6)
