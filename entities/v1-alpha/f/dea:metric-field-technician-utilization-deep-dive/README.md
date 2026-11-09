# dea:metric-field-technician-utilization-deep-dive

Candidate Performance Metric record for **Field Technician Utilization (Deep Dive)** (FTU-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-field-technician-utilization-deep-dive`
- **Name:** Field Technician Utilization (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FTU-D

## 2. Definition

Within Field Maintenance & Technical Field Service (Deep Dive), Field Technician Utilization (Deep Dive) (FTU-D) is used to gauge the utilization or availability of capacity. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Billable or Job Hours / Paid Hours, measured in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
FTU-D = Billable or Job Hours / Paid Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_maintenance_technical_field_service_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2912 (batch 7)
