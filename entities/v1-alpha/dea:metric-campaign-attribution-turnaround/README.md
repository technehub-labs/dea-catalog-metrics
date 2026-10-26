# dea:metric-campaign-attribution-turnaround

Candidate Performance Metric record for **Campaign Attribution Turnaround** (CAT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-campaign-attribution-turnaround`
- **Name:** Campaign Attribution Turnaround
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CAT

## 2. Definition

A Threat Intelligence & Red Team indicator, Campaign Attribution Turnaround (CAT) quantifies how efficiently resources are converted into outputs. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Days to Characterize Active Campaign - reported in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
CAT = Days to Characterize Active Campaign
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** risk
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** threat_intelligence_red_team

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3297 (batch 7)
