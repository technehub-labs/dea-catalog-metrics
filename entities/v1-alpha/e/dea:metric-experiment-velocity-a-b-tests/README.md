# dea:metric-experiment-velocity-a-b-tests

Candidate Performance Metric record for **Experiment Velocity (A/B Tests)** (EXV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-experiment-velocity-a-b-tests`
- **Name:** Experiment Velocity (A/B Tests)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EXV

## 2. Definition

Experiment Velocity (A/B Tests) (EXV) captures capability maturity or development for organizations tracking digital product & web operations. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Experiments Concluded with Decision per Period; the result is stated in count (items per period). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the number of experiments launched per period. It matters because sustained testing throughput is the operating cadence of a learning product organization. Volume can chase quantity over power, with under-sampled tests producing noise decisions. Read with Experiment Win Rate and shipped-change impact to confirm velocity converts into learning, not churn.

## Formula

```
EXV = Experiments Concluded with Decision per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** digital_product_web_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1087 (batch 4)
