# dea:metric-service-level-agreement-compliance

Candidate Performance Metric record for **Service Level Agreement Compliance** (SLA%) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-level-agreement-compliance`
- **Name:** Service Level Agreement Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SLA%

## 2. Definition

Service Level Agreement Compliance (SLA%) measures conformance to standards, plans, or obligations in the Customer domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Interactions Meeting SLA / Total Interactions; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
SLA% = Interactions Meeting SLA / Total Interactions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 82 (batch 1)
