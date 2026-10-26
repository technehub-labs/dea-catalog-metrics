# dea:metric-crisis-response-activation-time

Candidate Performance Metric record for **Crisis Response Activation Time** (CRAT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-crisis-response-activation-time`
- **Name:** Crisis Response Activation Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CRAT

## 2. Definition

A Business Resilience & Continuity indicator, Crisis Response Activation Time (CRAT) quantifies exposure to adverse outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Minutes from Trigger to Crisis Team Activated, measured in minutes. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures elapsed time from incident detection to crisis team activation with decision authority engaged. Slow activation wastes the golden window where incidents are cheap to contain, and it is a pure test of governance clarity rather than technology. Track separate clocks for detection-to-escalation and escalation-to-activation, since they fail for different reasons. Read with operational disruption loss value and post-incident activation reviews.

## Formula

```
Minutes from Trigger to Crisis Team Activated
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_resilience_continuity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1414 (batch 5)
