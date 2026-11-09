# dea:metric-pii-leakage-incidents-per-quarter

Candidate Performance Metric record for **PII Leakage Incidents per Quarter** (PIILQ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pii-leakage-incidents-per-quarter`
- **Name:** PII Leakage Incidents per Quarter
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PIILQ

## 2. Definition

A Generative AI & LLM Operations indicator, PII Leakage Incidents per Quarter (PIILQ) quantifies exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Incidents of Personal Data in Prompts or Outputs, expressed in count (items per period). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures occurrences of personal data exposure through model outputs or logs. LLMs leak PII through training-data memorization, prompt-retention, and logging pipelines, and each incident is simultaneously a privacy breach and a regulatory exposure under data protection regimes. Prevention coverage (input screening, output filters, log hygiene) matters more than detection speed here. Read with training-data PII scrubbing verification and retention-policy compliance.

## Formula

```
PIILQ = Incidents of Personal Data in Prompts or Outputs
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2551 (batch 7)
