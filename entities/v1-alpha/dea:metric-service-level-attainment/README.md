# dea:metric-service-level-attainment

Candidate Performance Metric record for **Service Level Attainment** (SLA-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-level-attainment`
- **Name:** Service Level Attainment
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SLA-T

## 2. Definition

A IT Service Management indicator, Service Level Attainment (SLA-T) quantifies conformance to standards, plans, or obligations. It is computed as Incidents Resolved within SLA / Total Incidents, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of intervals or events meeting committed service levels. It matters because SLAs are contractual promises whose breach carries penalties and churn risk. Gaming risk includes computing over generous windows, excluding declared-exception time, or scheduling to the metric rather than the need. Read with Customer Satisfaction Score and Cost per Contact trends to ensure SLA green is not bought with overstaffing.

## Formula

```
SLA-T = Incidents Resolved within SLA / Total Incidents
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 303 (batch 1)
