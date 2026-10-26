# dea:metric-field-service-cost-per-job-deep-dive

Candidate Performance Metric record for **Field Service Cost per Job (Deep Dive)** (FSCJ-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-field-service-cost-per-job-deep-dive`
- **Name:** Field Service Cost per Job (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FSCJ-D

## 2. Definition

Field Service Cost per Job (Deep Dive) (FSCJ-D) captures how efficiently resources are converted into outputs for organizations tracking field maintenance & technical field service (deep dive). Its calculation is Total Field Cost / Jobs Completed, measured in currency value. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the fully loaded cost per completed field job including labor, travel, parts, and overhead. It is the unit economics of field operations. Averages obscure travel-time differences between dense urban and rural territories. Read with truck roll resolution rate and schedule optimization savings.

## Formula

```
Total Field Cost / Jobs Completed
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_maintenance_technical_field_service_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2914 (batch 7)
