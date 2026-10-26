# dea:metric-remote-resolution-rate

Candidate Performance Metric record for **Remote Resolution Rate** (RRR-F) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-remote-resolution-rate`
- **Name:** Remote Resolution Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RRR-F

## 2. Definition

Within Field Service & Asset Performance, Remote Resolution Rate (RRR-F) is used to gauge how efficiently resources are converted into outputs. It is computed as Issues Resolved Remotely / Service Requests, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Issues Resolved Remotely / Service Requests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_service_asset_performance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3393 (batch 7)
