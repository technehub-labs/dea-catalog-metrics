# dea:metric-server-capacity-headroom-gaming

Candidate Performance Metric record for **Server Capacity Headroom (Gaming)** (SCH-G) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-server-capacity-headroom-gaming`
- **Name:** Server Capacity Headroom (Gaming)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SCH-G

## 2. Definition

Server Capacity Headroom (Gaming) (SCH-G) addresses the utilization or availability of capacity and is a fixture of gaming development & live operations reporting. It is computed as Peak Utilized Capacity / Provisioned Capacity, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is concentrated in Gaming.

## Formula

```
Peak Utilized Capacity / Provisioned Capacity
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** gaming_development_live_operations
- **Sector:** gaming

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1991 (batch 6)
