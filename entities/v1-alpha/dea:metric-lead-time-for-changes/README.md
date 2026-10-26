# dea:metric-lead-time-for-changes

Candidate Performance Metric record for **Lead Time for Changes** (LTDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-lead-time-for-changes`
- **Name:** Lead Time for Changes
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LTDC

## 2. Definition

Lead Time for Changes (LTDC) addresses how efficiently resources are converted into outputs and is a fixture of software engineering reporting. Its calculation is Median Time from Commit to Production, measured in hours. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Lead time for changes, one of the four DORA metrics, is the elapsed time from code committed to running in production. It measures flow, not speed of typing: a team can write code fast yet take weeks to ship it. Elite performers report under a day, low performers over a month. The classic move is to measure the median, exclude work-type outliers, and treat the distribution - not the average - as the truth: long-tail lead times are usually approval and queueing delays, which is exactly what DORA research says to attack.

## Formula

```
LTDC = Median Time from Commit to Production
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** DORA research program (DevOps Research and Assessment)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 278 (batch 1)
