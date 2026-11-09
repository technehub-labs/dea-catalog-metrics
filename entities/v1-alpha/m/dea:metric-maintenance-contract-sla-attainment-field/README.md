# dea:metric-maintenance-contract-sla-attainment-field

Candidate Performance Metric record for **Maintenance Contract SLA Attainment - Field** (MCSLAF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maintenance-contract-sla-attainment-field`
- **Name:** Maintenance Contract SLA Attainment - Field
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MCSLAF

## 2. Definition

A Field Maintenance & Technical Field Service (Deep Dive) indicator, Maintenance Contract SLA Attainment - Field (MCSLAF) quantifies conformance to standards, plans, or obligations. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Contracted Response SLAs Met / SLA Events - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of contract response and resolution commitments met across the field-maintained fleet. SLA attainment is the contractual heartbeat of service businesses, with penalties and renewals attached. Attainment through heroic overtime rather than capacity hides unsustainable performance. Read with maintenance contract renewal rate and first-time fix rate - field.

## Formula

```
MCSLAF = Contracted Response SLAs Met / SLA Events
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2922 (batch 7)
