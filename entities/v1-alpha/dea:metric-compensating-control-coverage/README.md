# dea:metric-compensating-control-coverage

Candidate Performance Metric record for **Compensating Control Coverage** (CCC-VM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-compensating-control-coverage`
- **Name:** Compensating Control Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCC-VM

## 2. Definition

Within Vulnerability & Exposure Management, Compensating Control Coverage (CCC-VM) is used to gauge exposure to adverse outcomes. The formula is Unpatched Systems with Compensating Controls / Unpatched Systems - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Unpatched Systems with Compensating Controls / Unpatched Systems
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** vulnerability_exposure_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2811 (batch 7)
