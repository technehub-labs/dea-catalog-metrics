# dea:metric-portfolio-risk-exposure-index

Candidate Performance Metric record for **Portfolio Risk Exposure Index** (PREI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-portfolio-risk-exposure-index`
- **Name:** Portfolio Risk Exposure Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PREI

## 2. Definition

Within PMO & Portfolio Governance, Portfolio Risk Exposure Index (PREI) is used to gauge exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Weighted Open Portfolio Risks vs Tolerance, expressed in index (0-100 or normalized). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures aggregated risk exposure across the portfolio, weighted by severity and proximity. The index is the early-warning system that turns project risks into portfolio decisions. Aggregation masks the few risks that warrant executive attention. Read with risk exposure trend index and project portfolio health distribution.

## Formula

```
PREI = Weighted Open Portfolio Risks vs Tolerance
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pmo_portfolio_governance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3411 (batch 7)
