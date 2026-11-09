# dea:metric-disparate-impact-ratio

Candidate Performance Metric record for **Disparate Impact Ratio** (DIR-AI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-disparate-impact-ratio`
- **Name:** Disparate Impact Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DIR-AI

## 2. Definition

Disparate Impact Ratio (DIR-AI) measures exposure to adverse outcomes in the AI Ethics, Fairness & Responsible AI domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Selection Rate of Protected Group / Reference Group, expressed in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the selection rate of the protected group against the majority group, benchmarked against the four-fifths rule used in employment law. It is the legally-anchored fairness screen, and it is the metric that converts statistical fairness into regulatory exposure analysis for hiring and credit decisions. The four-fifths threshold is guidance, not safe harbor, and relevant labor-market availability changes the read. Read with adverse impact analysis currency (Deep Dive) and job-relatedness validation evidence.

## Formula

```
DIR-AI = Selection Rate of Protected Group / Reference Group
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ai_ethics_fairness_responsible_ai

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2564 (batch 7)
