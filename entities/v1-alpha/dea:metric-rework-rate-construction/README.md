# dea:metric-rework-rate-construction

Candidate Performance Metric record for **Rework Rate (Construction)** (RWR-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rework-rate-construction`
- **Name:** Rework Rate (Construction)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RWR-C

## 2. Definition

Rework Rate (Construction) (RWR-C) addresses the quality of outputs and outcomes and is a fixture of construction & engineering reporting. It is defined as Value of Rework / Total Contract Value; the result is stated in percent (%). In Construction & engineering, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of work requiring redoing due to defects or nonconformance. It matters because rework consumes double resources and hides quality system failure. It can be gamed by classifying rework as new scope or including it in change orders. Read with Punch List size at handover and Cost Variance in Construction to confirm falling rework reflects better first-time quality.

## Formula

```
RWR-C = Value of Rework / Total Contract Value
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** construction_engineering
- **Sector:** construction_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 664 (batch 2)
