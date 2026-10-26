# dea:metric-hallucination-rate-per-1-000-responses

Candidate Performance Metric record for **Hallucination Rate per 1,000 Responses** (HALLR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hallucination-rate-per-1-000-responses`
- **Name:** Hallucination Rate per 1,000 Responses
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** HALLR

## 2. Definition

A Generative AI & LLM Operations indicator, Hallucination Rate per 1,000 Responses (HALLR) quantifies exposure to adverse outcomes. The formula is Responses Containing Fabricated Facts / 1,000 Responses - reported in events per thousand or million (scaled). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures frequency of fabricated or unsupported content in generations. Hallucination is the defining operational risk of generative AI in enterprise settings, and its rate - measured through grounding checks and sampled evaluation - determines which use cases are safely deployable. Rates vary enormously by task and retrieval quality, so report by use case, not blended. Read with grounded answer rate (Deep Dive) and evaluation harness coverage for regressions.

## Formula

```
Responses Containing Fabricated Facts / 1,000 Responses
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2538 (batch 7)
