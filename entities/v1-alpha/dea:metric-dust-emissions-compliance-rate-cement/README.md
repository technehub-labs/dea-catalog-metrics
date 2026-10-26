# dea:metric-dust-emissions-compliance-rate-cement

Candidate Performance Metric record for **Dust Emissions Compliance Rate (Cement)** (DECR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dust-emissions-compliance-rate-cement`
- **Name:** Dust Emissions Compliance Rate (Cement)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DECR

## 2. Definition

Within Cement & Building Materials, Dust Emissions Compliance Rate (Cement) (DECR) is used to gauge conformance to standards, plans, or obligations. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Stack Tests within Limits / Tests, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Manufacturing.

## 3. Context

Measures particulate emissions against permitted limits across stacks and fugitive sources. Cement is a visible-emissions industry where community complaints and enforcement track dust performance, and baghouse and ESP maintenance is the control discipline. Continuous monitor uptime is part of honest measurement. Read with complaint trends by neighborhood and filter media condition monitoring.

## Formula

```
DECR = Stack Tests within Limits / Tests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cement_building_materials
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1870 (batch 6)
