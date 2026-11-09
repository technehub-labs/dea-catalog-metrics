# dea:metric-inherent-availability

Candidate Performance Metric record for **Inherent Availability** (IAVL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-inherent-availability`
- **Name:** Inherent Availability
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IAVL

## 2. Definition

A Reliability & Maintainability Engineering (Deep Dive) indicator, Inherent Availability (IAVL) quantifies the quality of outputs and outcomes. It is defined as MTBF / (MTBF + MTTR); the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures achievable availability under ideal maintenance support (repair and logistics instantaneous). Inherent availability isolates design reliability and maintainability from support-system failures. Design fixes, not logistics fixes, move this number. Read with operational availability and mean time to repair - Field Assets (Deep Dive).

## Formula

```
IAVL = MTBF / (MTBF + MTTR)
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** reliability_maintainability_engineering_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4100 (batch 9)
