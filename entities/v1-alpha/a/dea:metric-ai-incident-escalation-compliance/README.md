# dea:metric-ai-incident-escalation-compliance

Candidate Performance Metric record for **AI Incident Escalation Compliance** (AIIEC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ai-incident-escalation-compliance`
- **Name:** AI Incident Escalation Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AIIEC

## 2. Definition

A AI Governance & Model Risk Management indicator, AI Incident Escalation Compliance (AIIEC) quantifies conformance to standards, plans, or obligations. It is defined as AI Incidents Escalated per Policy / Incidents; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether AI incidents (errors, harms, malfunctions) are escalated per policy and within timelines. Incident escalation is the AI equivalent of safety reporting: fast escalation enables containment and learning, while suppressed incidents accumulate into public failures and regulatory findings. Compliance requires clear incident definitions, which AI systems complicate with subtle degradation modes. Read with mean-time-to-escalate and post-incident review completion.

## Formula

```
AIIEC = AI Incidents Escalated per Policy / Incidents
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
- **Domain:** ai_governance_model_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2496 (batch 7)
