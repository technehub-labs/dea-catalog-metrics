# dea:metric-model-approval-gate-compliance

Candidate Performance Metric record for **Model Approval Gate Compliance** (MAGC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-approval-gate-compliance`
- **Name:** Model Approval Gate Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MAGC

## 2. Definition

A AI Governance & Model Risk Management indicator, Model Approval Gate Compliance (MAGC) quantifies conformance to standards, plans, or obligations. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Models Passing All Governance Gates before Deployment / Deployed, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether models passed required approval gates (design, validation sign-off, ethics review where applicable) before production use. Gate compliance is the control backbone of model governance: models deployed without gate approval are precisely the ones whose failure modes nobody reviewed, and AI regulation increasingly assumes these gates exist. Approval achieved through exception-granting escalation is compliance theater. Read with gate exception aging and post-deployment incident rates for excepted models.

## Formula

```
Models Passing All Governance Gates before Deployment / Deployed
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2489 (batch 7)
