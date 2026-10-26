# dea:metric-toxicity-rate-per-1-000-generations

Candidate Performance Metric record for **Toxicity Rate per 1,000 Generations** (TOXR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-toxicity-rate-per-1-000-generations`
- **Name:** Toxicity Rate per 1,000 Generations
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TOXR

## 2. Definition

Within Generative AI & LLM Operations, Toxicity Rate per 1,000 Generations (TOXR) is used to gauge exposure to adverse outcomes. It is computed as Generations Flagged Toxic / 1,000 Generations, expressed in events per thousand or million (scaled). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the frequency of harmful, biased, or inappropriate content in outputs. It is the brand-safety gate for generative deployments: a single viral toxic output can define the deployment publicly, and the rate is the leading indicator before users do the testing. Measurement must use the classifiers plus sampled human review, since classifiers miss context-dependent harm. Read with output-filter false-negative analysis and topic-domain risk segmentation.

## Formula

```
Generations Flagged Toxic / 1,000 Generations
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** generative_ai_llm_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2550 (batch 7)
