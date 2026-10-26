# dea:metric-llm-response-relevance-score

Candidate Performance Metric record for **LLM Response Relevance Score** (LLMRRS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-llm-response-relevance-score`
- **Name:** LLM Response Relevance Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LLMRRS

## 2. Definition

LLM Response Relevance Score (LLMRRS) measures the quality of outputs and outcomes in the Generative AI & LLM Operations domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Human-Rated Relevance Score per Response - reported in score (points). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how well model responses address the user's actual question or task. Relevance is the first-order quality gate of LLM deployments: fluent-but-wrong answers are worse than obviously-failed ones because users cannot distinguish them, and relevance scoring (human or model-graded against rubrics) is the ground truth for it. Rubric quality determines score meaning. Read with grounded answer rate (Deep Dive) and user satisfaction with AI assistant (Deep Dive).

## Formula

```
Human-Rated Relevance Score per Response
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2537 (batch 7)
