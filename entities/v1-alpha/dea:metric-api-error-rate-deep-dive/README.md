# dea:metric-api-error-rate-deep-dive

Candidate Performance Metric record for **API Error Rate (Deep Dive)** (APIER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-error-rate-deep-dive`
- **Name:** API Error Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** APIER

## 2. Definition

API Error Rate (Deep Dive) (APIER) addresses the quality of outputs and outcomes and is a fixture of api lifecycle management reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is 4xx+5xx Responses / Total API Responses - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Software sector.

## Formula

```
4xx+5xx Responses / Total API Responses
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** api_lifecycle_management
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3213 (batch 7)
