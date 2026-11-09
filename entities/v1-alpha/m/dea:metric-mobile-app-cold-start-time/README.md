# dea:metric-mobile-app-cold-start-time

Candidate Performance Metric record for **Mobile App Cold Start Time** (MACST) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mobile-app-cold-start-time`
- **Name:** Mobile App Cold Start Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MACST

## 2. Definition

Mobile App Cold Start Time (MACST) captures the quality of outputs and outcomes for organizations tracking mobile & client development. It is computed as Median Time to First Usable Screen on Launch, expressed in seconds. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is concentrated in Software.

## Formula

```
MACST = Median Time to First Usable Screen on Launch
```

## Unit

- **Unit reference:** `dea:unit-second`
- **Unit:** second
- **Unit label (as published):** seconds

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mobile_client_development
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3247 (batch 7)
