# dea:metric-llm-uptime-service-availability

Candidate Performance Metric record for **LLM Uptime - Service Availability** (LLMSA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-llm-uptime-service-availability`
- **Name:** LLM Uptime - Service Availability
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LLMSA

## 2. Definition

A Generative AI & LLM Operations indicator, LLM Uptime - Service Availability (LLMSA) quantifies the utilization or availability of capacity. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Assistant Available Time / Required Time, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Assistant Available Time / Required Time
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** generative_ai_llm_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2561 (batch 7)
