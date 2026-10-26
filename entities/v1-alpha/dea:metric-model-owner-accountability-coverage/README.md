# dea:metric-model-owner-accountability-coverage

Candidate Performance Metric record for **Model Owner Accountability Coverage** (MOAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-owner-accountability-coverage`
- **Name:** Model Owner Accountability Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MOAC

## 2. Definition

Model Owner Accountability Coverage (MOAC) measures governance in the AI Governance & Model Risk Management domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Models with Named Accountable Owner / Models - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of production models with a named, accountable owner. Ownership is the who-gets-called metric of governance: unowned models are unmaintained models, and accountability coverage is the organizational precondition for every other control. Owner in name only (a departed employee or an overloaded team) is the standard gap. Read with maintenance-activity evidence per owner and escalation path testing.

## Formula

```
Models with Named Accountable Owner / Models
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** governance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2499 (batch 7)
