# dea:metric-propensity-model-lift

Candidate Performance Metric record for **Propensity Model Lift** (PML) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-propensity-model-lift`
- **Name:** Propensity Model Lift
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PML

## 2. Definition

Propensity Model Lift (PML) measures the quality of outputs and outcomes in the Customer Analytics & Insights domain. The formula is Model Response Rate / Baseline Response Rate - reported in ratio (x:1 or x). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how much better a model identifies likely responders, churners, or defaulters than random targeting - the gain from concentrating effort on model-selected customers. It is the first-order proof an analytics investment pays, and the basis for campaign prioritization. Lift is strongest at the model's top deciles and degrades fast, so report lift at the operating depth actually used, not the best decile. Read with churn model recall and insight-to-action conversion.

## Formula

```
Model Response Rate / Baseline Response Rate
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** customer_analytics_insights

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1421 (batch 5)
