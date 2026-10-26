# dea:metric-interface-error-rate-deep-dive

Candidate Performance Metric record for **Interface Error Rate (Deep Dive)** (IER-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-interface-error-rate-deep-dive`
- **Name:** Interface Error Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** IER-D

## 2. Definition

Interface Error Rate (Deep Dive) (IER-D) addresses the quality of outputs and outcomes and is a fixture of erp & enterprise application operations reporting. It is a working-level control: thresholds trigger immediate operational response. It is defined as Failed Interface Messages / Messages; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Failed Interface Messages / Messages
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Domain:** erp_enterprise_application_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2170 (batch 6)
