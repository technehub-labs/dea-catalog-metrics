# dea:metric-monitoring-coverage-ratio

Candidate Performance Metric record for **Monitoring Coverage Ratio** (MONCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-monitoring-coverage-ratio`
- **Name:** Monitoring Coverage Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MONCR

## 2. Definition

Monitoring Coverage Ratio (MONCR) addresses capability maturity or development and is a fixture of network operations center (deep dive) reporting. The formula is Devices under Monitoring / In-Scope Devices - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of network elements under active monitoring. Coverage is the precondition for every other NOC metric: unmonitored equals unmanaged. Coverage of device up/down without performance and configuration telemetry is shallow. Read with unmonitored critical device count and service level indicator coverage.

## Formula

```
Devices under Monitoring / In-Scope Devices
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** network_operations_center_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2844 (batch 7)
