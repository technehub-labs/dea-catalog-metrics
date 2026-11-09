# dea:metric-api-consumer-onboarding-cycle-time

Candidate Performance Metric record for **API Consumer Onboarding Cycle Time** (APIONB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-consumer-onboarding-cycle-time`
- **Name:** API Consumer Onboarding Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** APIONB

## 2. Definition

Within API Lifecycle Management, API Consumer Onboarding Cycle Time (APIONB) is used to gauge how efficiently resources are converted into outputs. It is defined as Days from Key Request to Production Consumption; the result is stated in days. In Software, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
APIONB = Days from Key Request to Production Consumption
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3221 (batch 7)
