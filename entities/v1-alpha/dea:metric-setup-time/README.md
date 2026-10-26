# dea:metric-setup-time

Candidate Performance Metric record for **Setup Time** (SET) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-setup-time`
- **Name:** Setup Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SET

## 2. Definition

Setup Time (SET) captures how efficiently resources are converted into outputs for organizations tracking manufacturing. It is defined as Time to Prepare Equipment for Production Run; the result is stated in minutes. It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. In Manufacturing, it is a recognized element of the standard performance toolkit.

## Formula

```
Time to Prepare Equipment for Production Run
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 250 (batch 1)
