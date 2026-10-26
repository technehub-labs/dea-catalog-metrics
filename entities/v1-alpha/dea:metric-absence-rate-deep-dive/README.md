# dea:metric-absence-rate-deep-dive

Candidate Performance Metric record for **Absence Rate (Deep Dive)** (ARDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-absence-rate-deep-dive`
- **Name:** Absence Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ARDD

## 2. Definition

Within Workforce Planning & Productivity, Absence Rate (Deep Dive) (ARDD) is used to gauge the utilization or availability of capacity. It is defined as Absent Days / Scheduled Days; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
ARDD = Absent Days / Scheduled Days
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_productivity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3900 (batch 8)
