# dea:metric-ai-training-data-lineage-documentation-rate

Candidate Performance Metric record for **AI Training Data Lineage Documentation Rate** (AITDL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ai-training-data-lineage-documentation-rate`
- **Name:** AI Training Data Lineage Documentation Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AITDL

## 2. Definition

AI Training Data Lineage Documentation Rate (AITDL) addresses the quality of outputs and outcomes and is a fixture of ai governance & model risk management reporting. The formula is Datasets with Documented Lineage / Datasets Used - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of models with documented training-data provenance (sources, rights, processing, known biases). Lineage is the foundation under every downstream question - copyright disputes, bias findings, privacy breaches all resolve faster with it - and undocumented lineage converts routine questions into unanswerable liability. Documentation must be maintained through retraining, since lineage of the first version is not lineage of the current model. Read with third-party data rights verification and bias audit trail readiness.

## Formula

```
AITDL = Datasets with Documented Lineage / Datasets Used
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2504 (batch 7)
