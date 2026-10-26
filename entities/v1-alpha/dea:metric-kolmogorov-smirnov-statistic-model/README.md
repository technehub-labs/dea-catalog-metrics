# dea:metric-kolmogorov-smirnov-statistic-model

Candidate Performance Metric record for **Kolmogorov-Smirnov Statistic (Model)** (KSM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-kolmogorov-smirnov-statistic-model`
- **Name:** Kolmogorov-Smirnov Statistic (Model)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** KSM

## 2. Definition

Kolmogorov-Smirnov Statistic (Model) (KSM) captures the quality of outputs and outcomes for organizations tracking statistical model performance diagnostics. It is defined as Maximum Separation of Cumulative Event Distributions; the result is stated in percent (%). In Software, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The KS statistic, from Kolmogorov and Smirnov's distribution-test work, is the maximum gap between the cumulative distributions of good and bad scores - the point of best separation, expressed in percentage points. A KS of 40+ indicates a strong scorecard, 30-40 usable, under 20 weak. Credit and fraud shops love it because it names the score cutoff where separation peaks, which is directly actionable for threshold setting. Limitations: it looks only at the single worst-separated point, says nothing about the tails, and is sensitive to sample sizes - always report it with the decile chart.

## Formula

```
Maximum Separation of Cumulative Event Distributions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** statistical_model_performance_diagnostics
- **Sector:** software

## Attribution

- **Source credit:** Andrey Kolmogorov & Nikolai Smirnov

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4068 (batch 9)
