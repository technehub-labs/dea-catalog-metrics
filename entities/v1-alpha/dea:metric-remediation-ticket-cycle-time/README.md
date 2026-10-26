# dea:metric-remediation-ticket-cycle-time

Candidate Performance Metric record for **Remediation Ticket Cycle Time** (RTCVM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-remediation-ticket-cycle-time`
- **Name:** Remediation Ticket Cycle Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RTCVM

## 2. Definition

Remediation Ticket Cycle Time (RTCVM) captures how efficiently resources are converted into outputs for organizations tracking vulnerability & exposure management. It is defined as Days from Finding to Ticket Closure; the result is stated in days. It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Days from Finding to Ticket Closure
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** vulnerability_exposure_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2813 (batch 7)
