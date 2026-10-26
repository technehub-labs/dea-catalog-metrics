# dea:metric-audit-plan-completion

Candidate Performance Metric record for **Audit Plan Completion** (APC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-audit-plan-completion`
- **Name:** Audit Plan Completion
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** APC

## 2. Definition

Audit Plan Completion (APC) addresses conformance to standards, plans, or obligations and is a fixture of internal audit reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Audits Completed / Audits Planned, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The share of the planned audit engagements completed in the cycle - the delivery metric of the internal audit function, and the accountability measure that keeps the risk-based plan from being a wish: plans are built from the risk universe, and completion against plan is the evidence the function did what the risk assessment said mattered. Its strategic significance is the deviation-information it carries: engagements deferred are usually deferred for resource reasons, and the deferral pattern is itself a risk statement - which audits did the organization decide not to do, and what was happening in those areas while the audit waited. Read with the risk-ranked completion view: completing 95 percent of low-risk engagements while the high-risk ones deferred is schedule completion, not plan completion, and mature reporting weights the metric by plan-assigned risk hours.

## Formula

```
Audits Completed / Audits Planned
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_audit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 612 (batch 2)
