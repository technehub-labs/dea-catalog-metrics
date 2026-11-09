# dea:metric-application-response-time

Candidate Performance Metric record for **Application Response Time** (ART2) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-application-response-time`
- **Name:** Application Response Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ART2

## 2. Definition

Application Response Time (ART2) captures the quality of outputs and outcomes for organizations tracking it service management. It is a working-level control: thresholds trigger immediate operational response. It is defined as Median End-User Response Time; the result is stated in seconds. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
ART2 = Median End-User Response Time
```

## Unit

- **Unit reference:** `dea:unit-second`
- **Unit:** second
- **Unit label (as published):** seconds

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 316 (batch 1)
