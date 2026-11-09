# dea:metric-makeready-time

Candidate Performance Metric record for **Makeready Time** (MKT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-makeready-time`
- **Name:** Makeready Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MKT

## 2. Definition

Within Printing & Publishing, Makeready Time (MKT) is used to gauge how efficiently resources are converted into outputs. It is a working-level control: thresholds trigger immediate operational response. It is defined as Minutes to Set Up Job to Approved Standard; the result is stated in minutes. It should be driven down, since lower readings signal healthier performance. In Printing & publishing, it is a recognized element of the standard performance toolkit.

## Formula

```
MKT = Minutes to Set Up Job to Approved Standard
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
- **Domain:** printing_publishing
- **Sector:** printing_publishing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1259 (batch 4)
