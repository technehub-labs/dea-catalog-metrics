# dea:metric-process-standardization-prerequisite-rate

Candidate Performance Metric record for **Process Standardization Prerequisite Rate** (PSPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-standardization-prerequisite-rate`
- **Name:** Process Standardization Prerequisite Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PSPR

## 2. Definition

A Automation & Robotic Process Automation indicator, Process Standardization Prerequisite Rate (PSPR) quantifies conformance to standards, plans, or obligations. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Processes Standardized before Automation / Processes Automated; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of processes standardized before automation. It matters because automating a broken process just produces faster errors. Prerequisite checklists can be signed off without process actually being stable. Read with Human-in-the-Loop Intervention Rate and rework post-automation to confirm standardization was genuine.

## Formula

```
Processes Standardized before Automation / Processes Automated
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automation_robotic_process_automation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1333 (batch 5)
