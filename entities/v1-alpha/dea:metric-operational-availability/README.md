# dea:metric-operational-availability

Candidate Performance Metric record for **Operational Availability** (OPAVL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-operational-availability`
- **Name:** Operational Availability
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OPAVL

## 2. Definition

Operational Availability (OPAVL) addresses the quality of outputs and outcomes and is a fixture of reliability & maintainability engineering (deep dive) reporting. Its calculation is Uptime / (Uptime + Downtime all Causes), measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures actual availability including all waiting: parts, logistics, admin delays. Operational availability is what operations and customers actually experience. The gap to inherent availability quantifies the support system's tax. Read with inherent availability and maintenance contract SLA attainment - Field.

## Formula

```
Uptime / (Uptime + Downtime all Causes)
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4101 (batch 9)
