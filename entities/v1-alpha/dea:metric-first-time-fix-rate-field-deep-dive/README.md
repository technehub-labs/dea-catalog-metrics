# dea:metric-first-time-fix-rate-field-deep-dive

Candidate Performance Metric record for **First-Time Fix Rate - Field (Deep Dive)** (FTFR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-first-time-fix-rate-field-deep-dive`
- **Name:** First-Time Fix Rate - Field (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FTFR-D

## 2. Definition

First-Time Fix Rate - Field (Deep Dive) (FTFR-D) measures the quality of outputs and outcomes in the Field Maintenance & Technical Field Service (Deep Dive) domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Issues Resolved on First Visit / Field Jobs, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of field visits resolving the issue on the first appointment. Repeat visits double cost and destroy customer patience in on-site service businesses. Inflated rates follow when techs pre-close tickets remotely before true verification. Read with truck roll resolution rate and remote diagnostics resolution rate.

## Formula

```
Issues Resolved on First Visit / Field Jobs
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2904 (batch 7)
