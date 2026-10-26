# dea:metric-code-review-turnaround

Candidate Performance Metric record for **Code Review Turnaround** (CRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-code-review-turnaround`
- **Name:** Code Review Turnaround
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRT

## 2. Definition

Code Review Turnaround (CRT) captures how efficiently resources are converted into outputs for organizations tracking software engineering. The formula is Median Time from Pull Request to Review Completion - reported in hours. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
CRT = Median Time from Pull Request to Review Completion
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 290 (batch 1)
