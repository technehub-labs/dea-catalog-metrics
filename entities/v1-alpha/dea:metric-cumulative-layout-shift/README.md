# dea:metric-cumulative-layout-shift

Candidate Performance Metric record for **Cumulative Layout Shift** (CLS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cumulative-layout-shift`
- **Name:** Cumulative Layout Shift
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CLS

## 2. Definition

Cumulative Layout Shift (CLS) captures the quality of outputs and outcomes for organizations tracking digital product & web operations. It provides the day-to-day signal that a process is running as designed. Its calculation is Sum of Layout Instability Scores during Page Load, measured in score (points). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

CLS is a Google Web Vitals metric quantifying unexpected visual instability: how much visible content moves during load, scored from layout-shift data. Good is under 0.1; poor above 0.25. It captures the experience of buttons jumping as late-loading ads or images push content - the misclick problem - and unlike speed metrics it is about predictability rather than speed. Common fixes are explicit size attributes on media, reserved space for embeds, and avoiding content injected above existing content.

## Formula

```
Sum of Layout Instability Scores during Page Load
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1079 (batch 4)
