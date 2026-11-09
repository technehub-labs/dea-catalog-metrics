# dea:metric-change-request-cycle-time

Candidate Performance Metric record for **Change Request Cycle Time** (CRCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-change-request-cycle-time`
- **Name:** Change Request Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRCT

## 2. Definition

Within Project Management, Change Request Cycle Time (CRCT) is used to gauge how efficiently resources are converted into outputs. It is defined as Days from Change Request to Decision; the result is stated in days. It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
CRCT = Days from Change Request to Decision
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** transformation
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 361 (batch 1)
