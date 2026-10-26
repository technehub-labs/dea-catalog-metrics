# dea:metric-agent-occupancy-rate

Candidate Performance Metric record for **Agent Occupancy Rate** (AOR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-agent-occupancy-rate`
- **Name:** Agent Occupancy Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AOR

## 2. Definition

Agent Occupancy Rate (AOR) captures the utilization or availability of capacity for organizations tracking contact center. It is computed as Handle Time / Scheduled Time, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
AOR = Handle Time / Scheduled Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 566 (batch 2)
