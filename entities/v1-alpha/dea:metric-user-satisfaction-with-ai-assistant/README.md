# dea:metric-user-satisfaction-with-ai-assistant

Candidate Performance Metric record for **User Satisfaction with AI Assistant** (USA-AI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-user-satisfaction-with-ai-assistant`
- **Name:** User Satisfaction with AI Assistant
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** USA-AI

## 2. Definition

User Satisfaction with AI Assistant (USA-AI) addresses the engagement or satisfaction of the people involved and is a fixture of generative ai & llm operations reporting. Its calculation is Average CSAT for AI-Assisted Interactions, measured in score (points). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures user-rated experience with AI assistance. Satisfaction is the retention constraint of AI service: users tolerate imperfect automation that is fast and honest, but abandon evasive assistants and punish the brand attached to them. Measure satisfaction by resolution path (contained versus escalated) and by session outcome, since blended scores hide the frustrated cohort. Read with LLM containment rate (Deep Dive) and repeat-contact patterns.

## Formula

```
Average CSAT for AI-Assisted Interactions
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** engagement
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2548 (batch 7)
