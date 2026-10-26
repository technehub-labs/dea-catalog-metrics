# dea:metric-daily-commits-per-developer

Candidate Performance Metric record for **Daily Commits per Developer** (DCPD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-daily-commits-per-developer`
- **Name:** Daily Commits per Developer
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DCPD

## 2. Definition

Daily Commits per Developer (DCPD) addresses how efficiently resources are converted into outputs and is a fixture of continuous integration reporting. It is a working-level control: thresholds trigger immediate operational response. It is defined as Commits Merged per Developer per Day; the result is stated in count (items per period). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Commits Merged per Developer per Day
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_integration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2664 (batch 7)
