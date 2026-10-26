# dea:metric-insight-latency

Candidate Performance Metric record for **Insight Latency** (INS-L) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-insight-latency`
- **Name:** Insight Latency
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** INS-L

## 2. Definition

Insight Latency (INS-L) captures how efficiently resources are converted into outputs for organizations tracking customer analytics & insights. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Days from Data Availability to Insight Publication, expressed in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Days from Data Availability to Insight Publication
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** customer_analytics_insights

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1428 (batch 5)
