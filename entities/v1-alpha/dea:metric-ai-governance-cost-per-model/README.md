# dea:metric-ai-governance-cost-per-model

Candidate Performance Metric record for **AI Governance Cost per Model** (AIGCM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ai-governance-cost-per-model`
- **Name:** AI Governance Cost per Model
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AIGCM

## 2. Definition

AI Governance Cost per Model (AIGCM) addresses how efficiently resources are converted into outputs and is a fixture of ai governance & model risk management reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Governance and Validation Cost / Active Models, measured in currency value. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Governance and Validation Cost / Active Models
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ai_governance_model_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2511 (batch 7)
