# dea:metric-human-preference-win-rate-model-vs-baseline

Candidate Performance Metric record for **Human Preference Win Rate - Model vs Baseline** (HPWR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-human-preference-win-rate-model-vs-baseline`
- **Name:** Human Preference Win Rate - Model vs Baseline
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** HPWR

## 2. Definition

Within Generative AI & LLM Operations, Human Preference Win Rate - Model vs Baseline (HPWR) is used to gauge the quality of outputs and outcomes. It is defined as Blind Preferences for New Model / Total Evaluations; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how often evaluators prefer the candidate model's outputs over the incumbent's, using blind comparison. It is the deployment-decision workhorse of generative AI evaluation: aggregate benchmark scores correlate poorly with production experience, and blind human preference is the quality read that tracks user perception. Evaluator diversity and rubric quality determine validity. Read with production A/B outcome data - preference in evaluation should predict behavior in deployment.

## Formula

```
Blind Preferences for New Model / Total Evaluations
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** generative_ai_llm_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2549 (batch 7)
