# dea:metric-time-to-interactive

Candidate Performance Metric record for **Time to Interactive** (TTI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-interactive`
- **Name:** Time to Interactive
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TTI

## 2. Definition

A Digital Product & Web Operations indicator, Time to Interactive (TTI) quantifies the quality of outputs and outcomes. It is defined as Median Time until Page Fully Interactive; the result is stated in seconds. It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

TTI, from Google Web Vitals, measures when a page becomes reliably responsive - visually rendered, key handlers registered, and long tasks stopped delaying input. A page can look ready while remaining unusable (the classic spinner trap), and TTI was designed to expose that gap; good is under about 3.8 seconds on 4G. It is now partially superseded by INP for real interaction latency, but remains central to lab-based performance budgets and Lighthouse scoring.

## Formula

```
TTI = Median Time until Page Fully Interactive
```

## Unit

- **Unit reference:** `dea:unit-second`
- **Unit:** second
- **Unit label (as published):** seconds

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** digital_product_web_operations

## Attribution

- **Source credit:** Google Web Vitals

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1078 (batch 4)
