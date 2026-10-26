# dea:metric-hard-services-downtime-deep-dive

Candidate Performance Metric record for **Hard Services Downtime (Deep Dive)** (HSD-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hard-services-downtime-deep-dive`
- **Name:** Hard Services Downtime (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HSD-D

## 2. Definition

Hard Services Downtime (Deep Dive) (HSD-D) addresses exposure to adverse outcomes and is a fixture of facility management & workplace (deep dive) reporting. Its calculation is Hours of Critical System Downtime per Month, measured in hours. Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
HSD-D = Hours of Critical System Downtime per Month
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facility_management_workplace_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2245 (batch 6)
