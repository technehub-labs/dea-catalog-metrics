# dea:metric-alert-to-ticket-conversion-ratio

Candidate Performance Metric record for **Alert-to-Ticket Conversion Ratio** (ATTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-alert-to-ticket-conversion-ratio`
- **Name:** Alert-to-Ticket Conversion Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ATTR

## 2. Definition

A Network Operations Center (Deep Dive) indicator, Alert-to-Ticket Conversion Ratio (ATTR) quantifies how efficiently resources are converted into outputs. It is defined as Alerts Generating Tickets / Alerts; the result is stated in percent (%). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. Values outside the intended band, on either side, warrant investigation.

## Formula

```
ATTR = Alerts Generating Tickets / Alerts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** network_operations_center_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2842 (batch 7)
