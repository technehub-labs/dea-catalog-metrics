# dea:metric-model-inventory-completeness

Candidate Performance Metric record for **Model Inventory Completeness** (MIC-AI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-inventory-completeness`
- **Name:** Model Inventory Completeness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MIC-AI

## 2. Definition

Model Inventory Completeness (MIC-AI) addresses conformance to standards, plans, or obligations and is a fixture of ai governance & model risk management reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Documented Models in Inventory / Deployed Models - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of production models captured in the enterprise model inventory. The inventory is the foundation of all model risk management, and gaps are invisible ungoverned risk: untracked models make consequential decisions without validation, monitoring, or owner accountability. Completeness requires active discovery (code scanning, business attestation) rather than voluntary registration. Read with shadow AI detection ratio (Deep Dive) and model risk tiering coverage.

## Formula

```
MIC-AI = Documented Models in Inventory / Deployed Models
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2487 (batch 7)
