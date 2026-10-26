# dea:metric-meeting-room-utilization-deep-dive

Candidate Performance Metric record for **Meeting Room Utilization (Deep Dive)** (MRU-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-meeting-room-utilization-deep-dive`
- **Name:** Meeting Room Utilization (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MRU-D

## 2. Definition

Meeting Room Utilization (Deep Dive) (MRU-D) addresses the utilization or availability of capacity and is a fixture of facility management & workplace (deep dive) reporting. The formula is Booked Room Hours / Available Room Hours - reported in percent (%). It is applied across virtually every sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Booked Room Hours / Available Room Hours
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facility_management_workplace_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2243 (batch 6)
