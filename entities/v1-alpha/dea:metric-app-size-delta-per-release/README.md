# dea:metric-app-size-delta-per-release

Candidate Performance Metric record for **App Size Delta per Release** (ASDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-app-size-delta-per-release`
- **Name:** App Size Delta per Release
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ASDR

## 2. Definition

App Size Delta per Release (ASDR) captures how efficiently resources are converted into outputs for organizations tracking mobile & client development. It is a working-level control: thresholds trigger immediate operational response. It is defined as Change in Binary Size per Release; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. In Software, it is a recognized element of the standard performance toolkit.

## Formula

```
Change in Binary Size per Release
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mobile_client_development
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3258 (batch 7)
