# dea:metric-ai-benefit-realization-rate

Candidate Performance Metric record for **AI Benefit Realization Rate** (AIBRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ai-benefit-realization-rate`
- **Name:** AI Benefit Realization Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AIBRR

## 2. Definition

AI Benefit Realization Rate (AIBRR) addresses the economic value created or preserved and is a fixture of ai governance & model risk management reporting. The formula is Realized Benefits vs Business Case / Business Case - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of business cases for AI initiatives whose benefits were verified post-deployment. AI programs face the transformation value-gap problem with an added twist: hype inflates cases, and benefits are claimed from productivity that no budget line confirms. Finance-verified benefits against pre-agreed baselines are the only defensible realization measure. Read with cost avoidance validation and use-case portfolio ROI distribution.

## Formula

```
AIBRR = Realized Benefits vs Business Case / Business Case
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2506 (batch 7)
