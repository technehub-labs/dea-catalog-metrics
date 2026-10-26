# dea:metric-mean-time-between-failures-critical-assets

Candidate Performance Metric record for **Mean Time Between Failures (Critical Assets)** (MTBFCA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-between-failures-critical-assets`
- **Name:** Mean Time Between Failures (Critical Assets)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MTBFCA

## 2. Definition

Mean Time Between Failures (Critical Assets) (MTBFCA) addresses the quality of outputs and outcomes and is a fixture of field service & asset performance reporting. It is computed as Operating Hours / Failures for Critical Assets, expressed in hours. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures average operating time between failures for the most business-critical assets. MTBF for the critical few predicts the outages that actually cost money. Definitions of failure (degradation vs. stoppage) drive comparability. Read with preventive maintenance compliance - field and asset availability (Fleet Critical).

## Formula

```
Operating Hours / Failures for Critical Assets
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** operations
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_service_asset_performance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3394 (batch 7)
