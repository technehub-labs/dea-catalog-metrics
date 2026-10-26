# dea:metric-service-level-calls-answered-in-threshold-seconds

Candidate Performance Metric record for **Service Level - Calls Answered in Threshold Seconds** (SLDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-level-calls-answered-in-threshold-seconds`
- **Name:** Service Level - Calls Answered in Threshold Seconds
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SLDD

## 2. Definition

Service Level - Calls Answered in Threshold Seconds (SLDD) measures conformance to standards, plans, or obligations in the Contact Center Standard Measures (Deep Dive) domain. Its calculation is Calls Answered within Threshold / Calls Offered, measured in percent (%). It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Calls Answered within Threshold / Calls Offered
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4317 (batch 10)
