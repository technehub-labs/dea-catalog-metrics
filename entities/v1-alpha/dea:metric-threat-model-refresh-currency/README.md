# dea:metric-threat-model-refresh-currency

Candidate Performance Metric record for **Threat Model Refresh Currency** (TMFC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-threat-model-refresh-currency`
- **Name:** Threat Model Refresh Currency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TMFC

## 2. Definition

A Threat Intelligence & Red Team indicator, Threat Model Refresh Currency (TMFC) quantifies conformance to standards, plans, or obligations. The formula is Threat Models Refreshed within 12 Months / In-Scope Systems - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Threat Models Refreshed within 12 Months / In-Scope Systems
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** threat_intelligence_red_team

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3301 (batch 7)
