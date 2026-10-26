# dea:metric-data-subject-rights-request-timeliness-ai

Candidate Performance Metric record for **Data Subject Rights Request Timeliness - AI** (DSRTA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-subject-rights-request-timeliness-ai`
- **Name:** Data Subject Rights Request Timeliness - AI
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DSRTA

## 2. Definition

Data Subject Rights Request Timeliness - AI (DSRTA) measures conformance to standards, plans, or obligations in the AI Ethics, Fairness & Responsible AI domain. It is computed as Rights Requests Answered within Statutory Window / Requests, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether access, deletion, and correction requests touching AI systems are fulfilled within regulatory deadlines. AI complicates data subject rights: embedded data in models, inference stores, and logs create fulfillment paths that traditional privacy tooling misses, and deadlines treat AI complexity as no excuse. Measure the full fulfillment path including model-adjacent stores. Read with request-backlog aging and fulfillment completeness sampling.

## Formula

```
Rights Requests Answered within Statutory Window / Requests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ai_ethics_fairness_responsible_ai

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2568 (batch 7)
