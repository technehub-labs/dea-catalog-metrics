# dea:metric-system-availability-erp-deep-dive

Candidate Performance Metric record for **System Availability - ERP (Deep Dive)** (SAE-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-system-availability-erp-deep-dive`
- **Name:** System Availability - ERP (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SAE-D

## 2. Definition

A ERP & Enterprise Application Operations indicator, System Availability - ERP (Deep Dive) (SAE-D) quantifies the utilization or availability of capacity. Its calculation is Available Hours / Required Hours, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures ERP platform availability during business hours and batch windows. ERP downtime is enterprise-wide work stoppage - finance, order-to-cash, and supply all halt together - so availability carries compounding operational cost, and batch-window overruns are downtime even when the UI is up. Peak-period (month-end close) availability is the honest measurement focus. Read with batch-completion SLAs and incident-impact analysis.

## Formula

```
Available Hours / Required Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** erp_enterprise_application_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2176 (batch 6)
