# dea:metric-robot-mean-time-between-failures

Candidate Performance Metric record for **Robot Mean Time between Failures** (RMTBF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-robot-mean-time-between-failures`
- **Name:** Robot Mean Time between Failures
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RMTBF

## 2. Definition

Within Industrial Automation & Robotics, Robot Mean Time between Failures (RMTBF) is used to gauge exposure to adverse outcomes. The formula is Robot Operating Time / Robot Failures - reported in hours. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Manufacturing sector.

## 3. Context

Measures average uptime between robot failures. It matters because robot reliability determines whether automation reduces or complicates operations. MTBF can improve by counting only hard failures, ignoring degradation and micro-stops. Read with Automation Downtime Cost and minor-stop frequency to confirm reliability is honestly measured.

## Formula

```
Robot Operating Time / Robot Failures
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** industrial_automation_robotics
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1335 (batch 5)
