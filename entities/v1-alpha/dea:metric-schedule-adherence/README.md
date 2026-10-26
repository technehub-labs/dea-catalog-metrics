# dea:metric-schedule-adherence

Candidate Performance Metric record for **Schedule Adherence** (SA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-schedule-adherence`
- **Name:** Schedule Adherence
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SA

## 2. Definition

Schedule Adherence (SA) addresses conformance to standards, plans, or obligations and is a fixture of operations reporting. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Tasks Completed On Schedule / Tasks Scheduled; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how well frontline staff follow their planned schedules. It matters because forecasted service levels are unachievable if staffing does not match the plan. Gaming risk includes managers coding breaks flexibly to keep the metric green. Read with Forecast Accuracy and Service Level Attainment to confirm adherence discipline actually converts into service outcomes.

## Formula

```
Tasks Completed On Schedule / Tasks Scheduled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 154 (batch 1)
