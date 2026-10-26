# dea:metric-human-in-the-loop-coverage-for-high-risk-decisions

Candidate Performance Metric record for **Human-in-the-Loop Coverage for High-Risk Decisions** (HITC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-human-in-the-loop-coverage-for-high-risk-decisions`
- **Name:** Human-in-the-Loop Coverage for High-Risk Decisions
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** HITC

## 2. Definition

Human-in-the-Loop Coverage for High-Risk Decisions (HITC) addresses exposure to adverse outcomes and is a fixture of ai governance & model risk management reporting. It is computed as High-Risk Decision Points with Human Review / High-Risk Points, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of high-risk AI decisions retaining meaningful human review before effect. Human oversight is the regulatory expectation for consequential decisions (credit, employment, safety), and coverage questions whether review is meaningful - rubber-stamp approval of automated recommendations is human-in-name-only. Review capacity and override rates are the honesty probes: reviewers who never override are not reviewing. Read with override-rate distributions and reviewer workload metrics.

## Formula

```
High-Risk Decision Points with Human Review / High-Risk Points
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ai_governance_model_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2495 (batch 7)
