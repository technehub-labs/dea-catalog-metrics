# dea:metric-cost-per-1-000-inference-tokens

Candidate Performance Metric record for **Cost per 1,000 Inference Tokens** (CP1KT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-1-000-inference-tokens`
- **Name:** Cost per 1,000 Inference Tokens
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CP1KT

## 2. Definition

Cost per 1,000 Inference Tokens (CP1KT) measures how efficiently resources are converted into outputs in the Generative AI & LLM Operations domain. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Inference Spend / 1,000 Tokens Processed, expressed in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
CP1KT = Inference Spend / 1,000 Tokens Processed
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** generative_ai_llm_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2554 (batch 7)
