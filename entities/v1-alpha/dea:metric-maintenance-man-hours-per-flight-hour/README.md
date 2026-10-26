# dea:metric-maintenance-man-hours-per-flight-hour

Candidate Performance Metric record for **Maintenance Man-Hours per Flight Hour** (MMHF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maintenance-man-hours-per-flight-hour`
- **Name:** Maintenance Man-Hours per Flight Hour
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MMHF

## 2. Definition

Maintenance Man-Hours per Flight Hour (MMHF) addresses how efficiently resources are converted into outputs and is a fixture of defense & aerospace reporting. It is defined as Maintenance Hours / Flight Hours; the result is stated in ratio (x:1 or x). In Defense & aerospace, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures maintenance labor consumed per aircraft flight hour. It matters because it is the core efficiency ratio for defense and commercial aviation fleet sustainment. Man-hours can be cut by deferring inspections that surface as availability loss later. Read with Equipment Availability trends and Mean Time Between Failure for the fleet to confirm efficiency is not borrowing reliability.

## Formula

```
Maintenance Hours / Flight Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** defense_aerospace
- **Sector:** defense_aerospace

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 971 (batch 3)
