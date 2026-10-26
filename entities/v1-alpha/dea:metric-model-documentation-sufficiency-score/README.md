# dea:metric-model-documentation-sufficiency-score

Candidate Performance Metric record for **Model Documentation Sufficiency Score** (MDSS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-documentation-sufficiency-score`
- **Name:** Model Documentation Sufficiency Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MDSS

## 2. Definition

Model Documentation Sufficiency Score (MDSS) addresses the quality of outputs and outcomes and is a fixture of ai governance & model risk management reporting. Its calculation is Documentation Items Complete / Required per Policy, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether model documentation meets the standard (purpose, methodology, assumptions, limitations, performance). Documentation is the transferability layer of model governance - validators, auditors, and successors all depend on it - and insufficient documentation converts personnel turnover into model risk. Scoring must be against the documented standard with evidence, not existence-of-document checks. Read with validation findings on documentation and time-to-onboard for new model owners.

## Formula

```
Documentation Items Complete / Required per Policy
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2490 (batch 7)
