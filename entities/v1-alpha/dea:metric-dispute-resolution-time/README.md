# dea:metric-dispute-resolution-time

Candidate Performance Metric record for **Dispute Resolution Time** (DRT-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dispute-resolution-time`
- **Name:** Dispute Resolution Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DRT-P

## 2. Definition

A Payments & Fintech indicator, Dispute Resolution Time (DRT-P) quantifies how efficiently resources are converted into outputs. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Days from Dispute Raised to Resolution, measured in days. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Payments & fintech practice.

## 3. Context

Measures average time to resolve payment disputes or chargebacks. It matters because disputes freeze funds and drive processor-risk assessments. Resolution speed can be achieved by conceding disputes to close them, buying the metric with revenue. Read with Dispute Loss Rate and Win Rate on Representment to confirm fast resolution is also favorable.

## Formula

```
Days from Dispute Raised to Resolution
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** payments_fintech
- **Sector:** payments_fintech

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 783 (batch 2)
