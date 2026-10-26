# dea:metric-hotel-rate-variance-to-corporate-rate

Candidate Performance Metric record for **Hotel Rate Variance to Corporate Rate** (HRVC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hotel-rate-variance-to-corporate-rate`
- **Name:** Hotel Rate Variance to Corporate Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** HRVC

## 2. Definition

Hotel Rate Variance to Corporate Rate (HRVC) measures the economic value created or preserved in the Corporate Travel Management domain. Its calculation is Average Paid Rate - Negotiated Rate, Averaged, measured in currency per unit. It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Average Paid Rate - Negotiated Rate, Averaged
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** organization
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_travel_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1220 (batch 4)
