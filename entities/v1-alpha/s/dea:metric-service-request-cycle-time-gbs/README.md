# dea:metric-service-request-cycle-time-gbs

Candidate Performance Metric record for **Service Request Cycle Time (GBS)** (SRCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-request-cycle-time-gbs`
- **Name:** Service Request Cycle Time (GBS)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SRCT

## 2. Definition

A Shared Services & Global Business Services indicator, Service Request Cycle Time (GBS) (SRCT) quantifies how efficiently resources are converted into outputs. It is defined as Hours from Request to Fulfillment; the result is stated in hours. It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
SRCT = Hours from Request to Fulfillment
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** shared_services_global_business_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1052 (batch 4)
