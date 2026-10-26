# dea:metric-maintenance-related-cancellation-rate

Candidate Performance Metric record for **Maintenance-Related Cancellation Rate** (MRCR-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maintenance-related-cancellation-rate`
- **Name:** Maintenance-Related Cancellation Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MRCR-A

## 2. Definition

A Airline Operations (Deep Dive) indicator, Maintenance-Related Cancellation Rate (MRCR-A) quantifies exposure to adverse outcomes. It is computed as Cancellations Due to Maintenance / Schedules, expressed in percent (%). Its use is concentrated in Airlines. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures cancellations attributable to technical causes. It is the customer-facing cost of fleet and engineering performance, and it is cyclical with fleet age, maintenance program changes, and parts supply - grounded aircraft while owning the schedule is the most expensive operational state. Root-cause distribution (planned versus unplanned, AOG parts versus labor) directs the fix. Read with technical dispatch reliability (Deep Dive) and AOG recovery times.

## Formula

```
Cancellations Due to Maintenance / Schedules
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2258 (batch 6)
