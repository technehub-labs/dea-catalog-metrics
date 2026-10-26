# dea:metric-process-cycle-time

Candidate Performance Metric record for **Process Cycle Time** (PCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-cycle-time`
- **Name:** Process Cycle Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PCT

## 2. Definition

A Operations indicator, Process Cycle Time (PCT) quantifies how efficiently resources are converted into outputs. It is a working-level control: thresholds trigger immediate operational response. It is defined as End-to-End Elapsed Time of Process; the result is stated in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
End-to-End Elapsed Time of Process
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 155 (batch 1)
