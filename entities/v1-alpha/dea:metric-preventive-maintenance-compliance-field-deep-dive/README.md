# dea:metric-preventive-maintenance-compliance-field-deep-dive

Candidate Performance Metric record for **Preventive Maintenance Compliance - Field (Deep Dive)** (PMCF-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-preventive-maintenance-compliance-field-deep-dive`
- **Name:** Preventive Maintenance Compliance - Field (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PMCF-D

## 2. Definition

A Field Maintenance & Technical Field Service (Deep Dive) indicator, Preventive Maintenance Compliance - Field (Deep Dive) (PMCF-D) quantifies conformance to standards, plans, or obligations. It is defined as Field PM Tasks Completed on Schedule / Scheduled; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of scheduled preventive visits completed on time. Prevention is the cheapest form of field service: each PM visit avoids multiples of corrective cost and downtime. Compliance measured as rescheduled rather than completed hides deferral. Read with corrective-to-preventive work ratio and contract renewal rate - maintenance contracts.

## Formula

```
PMCF-D = Field PM Tasks Completed on Schedule / Scheduled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_maintenance_technical_field_service_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2907 (batch 7)
