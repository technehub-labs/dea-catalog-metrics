# dea:metric-zero-day-response-time

Candidate Performance Metric record for **Zero-Day Response Time** (ZDRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-zero-day-response-time`
- **Name:** Zero-Day Response Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ZDRT

## 2. Definition

A Vulnerability & Exposure Management indicator, Zero-Day Response Time (ZDRT) quantifies how efficiently resources are converted into outputs. The formula is Hours from Zero-Day Advisory to Mitigation - reported in hours. It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures elapsed time from zero-day disclosure (or in-the-wild exploitation) to protective mitigation across the estate. Zero-days compress every other timeline; rehearsed emergency patching is the only response. Measured from internal awareness rather than public disclosure flatters the number. Read with internet-facing critical exposure time and emergency release ratio.

## Formula

```
Hours from Zero-Day Advisory to Mitigation
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** vulnerability_exposure_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2814 (batch 7)
