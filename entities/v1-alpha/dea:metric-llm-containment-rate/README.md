# dea:metric-llm-containment-rate

Candidate Performance Metric record for **LLM Containment Rate** (LLMCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-llm-containment-rate`
- **Name:** LLM Containment Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LLMCR

## 2. Definition

A Generative AI & LLM Operations indicator, LLM Containment Rate (LLMCR) quantifies how efficiently resources are converted into outputs. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Conversations Completed without Escalation / Conversations, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of conversations completed by the AI assistant without human escalation. It is the efficiency headline of conversational AI deployments, and it is only honest alongside quality: containment achieved by refusing to escalate (no escape hatch, dead-end loops) is containment of complaints, not of work. Containment-quality pairing with satisfaction and repeat contact is mandatory. Read with user satisfaction with AI assistant (Deep Dive) and escalation-reason analysis.

## Formula

```
LLMCR = Conversations Completed without Escalation / Conversations
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2547 (batch 7)
