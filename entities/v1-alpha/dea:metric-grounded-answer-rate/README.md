# dea:metric-grounded-answer-rate

Candidate Performance Metric record for **Grounded Answer Rate** (GAR-LLM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-grounded-answer-rate`
- **Name:** Grounded Answer Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** GAR-LLM

## 2. Definition

A Generative AI & LLM Operations indicator, Grounded Answer Rate (GAR-LLM) quantifies the quality of outputs and outcomes. It is defined as Responses Fully Grounded in Retrieved Context / Responses; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of responses fully supported by cited source material. Grounding is the enterprise control for hallucination: retrieval-based answers that trace to sources are auditable and defensible, and the grounded rate is the deployability metric for regulated or high-stakes text. Grounding claims must verify citation accuracy, since plausible-but-wrong citations are hallucination in a suit. Read with hallucination rate per 1,000 responses (Deep Dive) and source-quality screening.

## Formula

```
Responses Fully Grounded in Retrieved Context / Responses
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2539 (batch 7)
