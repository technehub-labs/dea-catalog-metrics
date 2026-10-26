# dea:metric-llm-token-cost-per-resolution

Candidate Performance Metric record for **LLM Token Cost per Resolution** (LLMTCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-llm-token-cost-per-resolution`
- **Name:** LLM Token Cost per Resolution
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LLMTCR

## 2. Definition

A Generative AI & LLM Operations indicator, LLM Token Cost per Resolution (LLMTCR) quantifies how efficiently resources are converted into outputs. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Token and Inference Cost / Resolved Interactions; the result is stated in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures token and serving cost per successfully resolved user task. It is the unit-economics metric of LLM-powered service: token costs at scale are material, and cost per resolution (not per interaction) prices the value actually delivered. Resolutions that shift cost to human escalation make the metric worse, so read jointly with containment. Read with LLM containment rate (Deep Dive) and assistant deflection value (Deep Dive).

## Formula

```
Token and Inference Cost / Resolved Interactions
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** generative_ai_llm_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2543 (batch 7)
