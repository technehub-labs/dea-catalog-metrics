# dea:metric-api-time-to-first-hello

Candidate Performance Metric record for **API Time to First Hello** (TTFH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-time-to-first-hello`
- **Name:** API Time to First Hello
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TTFH

## 2. Definition

API Time to First Hello (TTFH) addresses how efficiently resources are converted into outputs and is a fixture of api lifecycle management reporting. It is computed as Median Minutes for New Consumer to Make Successful Call, expressed in minutes. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is concentrated in Software.

## Formula

```
Median Minutes for New Consumer to Make Successful Call
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** api_lifecycle_management
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3212 (batch 7)
