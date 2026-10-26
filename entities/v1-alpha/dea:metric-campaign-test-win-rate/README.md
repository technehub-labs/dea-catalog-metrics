# dea:metric-campaign-test-win-rate

Candidate Performance Metric record for **Campaign Test Win Rate** (CTWR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-campaign-test-win-rate`
- **Name:** Campaign Test Win Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CTWR

## 2. Definition

Within Customer Analytics & Insights, Campaign Test Win Rate (CTWR) is used to gauge how effectively a process or entity achieves its intended outcome. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Tests Where Variant Beats Control / Tests Concluded, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of marketing tests producing significant winners. It matters because win rates reveal both creative quality and testing discipline. A too-high win rate suggests under-powered tests declaring noise as wins. Read with Experiment Velocity (A/B Tests) and minimum detectable effect standards to confirm wins are statistically real.

## Formula

```
Tests Where Variant Beats Control / Tests Concluded
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** customer_analytics_insights

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1422 (batch 5)
