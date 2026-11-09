# dea:metric-alarm-false-callout-rate

Candidate Performance Metric record for **Alarm False Callout Rate** (AFCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-alarm-false-callout-rate`
- **Name:** Alarm False Callout Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AFCR

## 2. Definition

Alarm False Callout Rate (AFCR) addresses how efficiently resources are converted into outputs and is a fixture of security services & guarding reporting. It is defined as False Alarm Responses / Alarm Responses; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. In Security, it is a recognized element of the standard performance toolkit.

## Formula

```
AFCR = False Alarm Responses / Alarm Responses
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** security_services_guarding
- **Sector:** security

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2057 (batch 6)
