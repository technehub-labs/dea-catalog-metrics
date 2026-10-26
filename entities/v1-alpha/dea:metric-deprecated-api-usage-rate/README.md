# dea:metric-deprecated-api-usage-rate

Candidate Performance Metric record for **Deprecated API Usage Rate** (DAUR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deprecated-api-usage-rate`
- **Name:** Deprecated API Usage Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DAUR

## 2. Definition

Deprecated API Usage Rate (DAUR) addresses exposure to adverse outcomes and is a fixture of software development - coding & engineering practices reporting. It is computed as Calls to Deprecated APIs / Total Internal API Calls, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Calls to Deprecated APIs / Total Internal API Calls
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** software_development_coding_engineering_practices

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2659 (batch 7)
