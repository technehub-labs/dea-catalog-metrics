# dea:metric-average-journey-cycle-time

Candidate Performance Metric record for **Average Journey Cycle Time** (AJCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-journey-cycle-time`
- **Name:** Average Journey Cycle Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AJCT

## 2. Definition

A Customer Journey & Experience indicator, Average Journey Cycle Time (AJCT) quantifies how efficiently resources are converted into outputs. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Total Time across Journey Stages / Completed Journeys, expressed in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures mean elapsed time to complete a defined customer journey end to end. It matters because journey duration is the customer-felt sum of all internal handoffs. Clock definitions can start late (after first login) to shrink the measured time. Read with Journey Drop-off Rate by Stage and First Contact Resolution to locate whether time is genuine or definitionally trimmed.

## Formula

```
Total Time across Journey Stages / Completed Journeys
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_journey_experience

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1250 (batch 4)
