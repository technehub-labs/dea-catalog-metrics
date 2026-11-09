# dea:metric-pull-request-cycle-time

Candidate Performance Metric record for **Pull Request Cycle Time** (PRCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pull-request-cycle-time`
- **Name:** Pull Request Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PRCT

## 2. Definition

Pull Request Cycle Time (PRCT) addresses how efficiently resources are converted into outputs and is a fixture of software engineering reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Median Time from PR Open to Merge - reported in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
PRCT = Median Time from PR Open to Merge
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 291 (batch 1)
