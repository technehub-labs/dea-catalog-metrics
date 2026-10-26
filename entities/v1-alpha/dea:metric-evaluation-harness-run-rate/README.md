# dea:metric-evaluation-harness-run-rate

Candidate Performance Metric record for **Evaluation Harness Run Rate** (EHRR-LLM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-evaluation-harness-run-rate`
- **Name:** Evaluation Harness Run Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EHRR-LLM

## 2. Definition

Evaluation Harness Run Rate (EHRR-LLM) addresses conformance to standards, plans, or obligations and is a fixture of generative ai & llm operations reporting. Its calculation is Model Releases Evaluated before Deployment / Releases, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the cadence and coverage of automated evaluation runs against the model's task suite. The evaluation harness is the regression-test layer of LLM operations: prompts, models, and retrieval sources all change, and silent quality decay is only caught by disciplined evaluation runs. Coverage must span task-representative suites, not cherry-picked demos. Read with regression rates caught pre-release and production-quality drift correlation.

## Formula

```
EHRR-LLM = Model Releases Evaluated before Deployment / Releases
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2553 (batch 7)
