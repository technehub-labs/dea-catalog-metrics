# dea:metric-model-risk-tiering-coverage

Candidate Performance Metric record for **Model Risk Tiering Coverage** (MRTC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-risk-tiering-coverage`
- **Name:** Model Risk Tiering Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MRTC

## 2. Definition

A AI Governance & Model Risk Management indicator, Model Risk Tiering Coverage (MRTC) quantifies exposure to adverse outcomes. It is computed as Models Assigned Risk Tier / Models in Inventory, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of inventory models classified by materiality and risk. Tiering allocates governance resources proportionately - high-risk models get deep validation and monitoring while low-risk models get lightweight treatment - and un-tiered models default to nobody's attention. Tiering criteria must be objective enough to audit, since tier downgrade is the subtle way model owners escape scrutiny. Read with model inventory completeness and validation resource allocation against tier distribution.

## Formula

```
Models Assigned Risk Tier / Models in Inventory
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2488 (batch 7)
