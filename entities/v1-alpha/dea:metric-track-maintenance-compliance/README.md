# dea:metric-track-maintenance-compliance

Candidate Performance Metric record for **Track Maintenance Compliance** (TMC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-track-maintenance-compliance`
- **Name:** Track Maintenance Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TMC

## 2. Definition

Track Maintenance Compliance (TMC) captures conformance to standards, plans, or obligations for organizations tracking rail transport. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Maintenance Tasks Completed on Schedule / Tasks Planned, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Rail practice.

## 3. Context

Measures completion of scheduled track maintenance against plan. It matters because deferred track work compounds into speed restrictions and derailment risk. Work can be closed administratively while quality standards are unmet. Read with Track Defect Rate and Speed Restriction hours to confirm maintenance discipline converts into network performance.

## Formula

```
TMC = Maintenance Tasks Completed on Schedule / Tasks Planned
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_transport
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 996 (batch 3)
