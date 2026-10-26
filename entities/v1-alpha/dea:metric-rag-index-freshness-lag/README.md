# dea:metric-rag-index-freshness-lag

Candidate Performance Metric record for **RAG Index Freshness Lag** (RAGIFL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rag-index-freshness-lag`
- **Name:** RAG Index Freshness Lag
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RAGIFL

## 2. Definition

RAG Index Freshness Lag (RAGIFL) measures the quality of outputs and outcomes in the Generative AI & LLM Operations domain. Its calculation is Hours between Source Update and Index Refresh, measured in hours. It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
RAGIFL = Hours between Source Update and Index Refresh
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** generative_ai_llm_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2556 (batch 7)
