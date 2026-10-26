# dea:metric-prompt-injection-block-rate

Candidate Performance Metric record for **Prompt Injection Block Rate** (PIBR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-prompt-injection-block-rate`
- **Name:** Prompt Injection Block Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PIBR

## 2. Definition

Prompt Injection Block Rate (PIBR) measures exposure to adverse outcomes in the Generative AI & LLM Operations domain. It is defined as Malicious Prompts Blocked by Guardrails / Malicious Prompts Detected; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of injection attacks neutralized by input controls. Prompt injection is the dominant security risk of deployed LLMs - adversarial inputs that redirect model behavior - and the block rate is the defensive efficacy metric for a threat class that standard web security does not cover. Testing must include both direct and indirect injection (malicious content inside retrieved documents). Read with red-team test coverage and data-exfiltration attempt monitoring.

## Formula

```
Malicious Prompts Blocked by Guardrails / Malicious Prompts Detected
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2540 (batch 7)
