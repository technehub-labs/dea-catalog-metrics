# dea:metric-data-subject-request-fulfilment-rate

Candidate Performance Metric record for **Data Subject Request Fulfilment Rate** (DSRFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-subject-request-fulfilment-rate`
- **Name:** Data Subject Request Fulfilment Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DSRFR

## 2. Definition

A Data Privacy & Protection indicator, Data Subject Request Fulfilment Rate (DSRFR) quantifies conformance to standards, plans, or obligations. The formula is DSARs Fulfilled within Statutory Time / DSARs - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how completely and timely access, deletion, and portability requests are fulfilled. DSARs are the most operational privacy duty, with statutory clocks. Fulfilment that misses shadow data copies is incomplete compliance. Read with data subject request cycle time and privacy breach notification timeliness.

## Formula

```
DSRFR = DSARs Fulfilled within Statutory Time / DSARs
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_privacy_protection

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3657 (batch 8)
