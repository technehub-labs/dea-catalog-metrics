# dea:metric-error-rate-http-5xx

Candidate Performance Metric record for **Error Rate (HTTP 5xx)** (ERR5) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-error-rate-http-5xx`
- **Name:** Error Rate (HTTP 5xx)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ERR5

## 2. Definition

Error Rate (HTTP 5xx) (ERR5) measures the quality of outputs and outcomes in the Digital Product & Web Operations domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Server Error Responses / Total Responses; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
ERR5 = Server Error Responses / Total Responses
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** digital_product_web_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1077 (batch 4)
