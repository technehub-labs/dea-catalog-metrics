# dea:metric-model-validation-cycle-currency

Candidate Performance Metric record for **Model Validation Cycle Currency** (MVCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-validation-cycle-currency`
- **Name:** Model Validation Cycle Currency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MVCC

## 2. Definition

Model Validation Cycle Currency (MVCC) measures conformance to standards, plans, or obligations in the AI Governance & Model Risk Management domain. The formula is Validations within Recurrent Cycle / Due in Period - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether validations are current against required periodicity. Model performance decays through drift and population change, and stale validations certify yesterday's model. Currency gaps cluster on models owned by teams that restructured, which is the audit finding pattern. Read with data drift detection coverage (Deep Dive) and re-prioritization of validation queues by materiality.

## Formula

```
MVCC = Validations within Recurrent Cycle / Due in Period
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2492 (batch 7)
