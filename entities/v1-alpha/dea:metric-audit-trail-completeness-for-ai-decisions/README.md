# dea:metric-audit-trail-completeness-for-ai-decisions

Candidate Performance Metric record for **Audit Trail Completeness for AI Decisions** (ATCAD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-audit-trail-completeness-for-ai-decisions`
- **Name:** Audit Trail Completeness for AI Decisions
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ATCAD

## 2. Definition

A AI Governance & Model Risk Management indicator, Audit Trail Completeness for AI Decisions (ATCAD) quantifies conformance to standards, plans, or obligations. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Decisions with Complete Audit Trail / Decisions Sampled - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether automated decisions are logged with inputs, model version, outputs, and rationale. Complete audit trails are the retrospective accountability layer: investigations, disputes, and regulatory examinations all require reconstructing what the system decided and why, and gaps convert incidents into unanswerable questions. Logging must capture the actual decision context, including input data as it was at decision time. Read with log retention compliance and reconstruction test results.

## Formula

```
Decisions with Complete Audit Trail / Decisions Sampled
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Domain:** ai_governance_model_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2503 (batch 7)
