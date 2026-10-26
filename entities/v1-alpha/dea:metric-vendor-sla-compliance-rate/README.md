# dea:metric-vendor-sla-compliance-rate

Candidate Performance Metric record for **Vendor SLA Compliance Rate** (VSCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vendor-sla-compliance-rate`
- **Name:** Vendor SLA Compliance Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VSCR

## 2. Definition

A Outsourcing & Vendor Management indicator, Vendor SLA Compliance Rate (VSCR) quantifies conformance to standards, plans, or obligations. Its calculation is Vendor Deliveries Meeting SLA / Vendor Deliveries Measured, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of vendor obligations meeting contracted service levels. It matters because SLA enforcement is the practical control over outsourced quality. Vendors can meet letter-of-contract SLAs while true service quality declines. Read with Vendor Quality Scorecard Average and business-outcome metrics to confirm compliance reflects delivered value.

## Formula

```
Vendor Deliveries Meeting SLA / Vendor Deliveries Measured
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** outsourcing_vendor_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1124 (batch 4)
