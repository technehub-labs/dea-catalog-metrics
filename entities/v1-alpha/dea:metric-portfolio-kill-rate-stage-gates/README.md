# dea:metric-portfolio-kill-rate-stage-gates

Candidate Performance Metric record for **Portfolio Kill-Rate (Stage Gates)** (PKRG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-portfolio-kill-rate-stage-gates`
- **Name:** Portfolio Kill-Rate (Stage Gates)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PKRG

## 2. Definition

Portfolio Kill-Rate (Stage Gates) (PKRG) measures governance in the PMO & Portfolio Governance domain. It is computed as Initiatives Stopped at Gate / Initiatives Reviewed, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of initiatives stopped at or between stage gates. A nonzero kill-rate is a sign of health: it means gates actually gate. Chronic zero kill-rate means the gate review has never met a project it didn't like. Read with initiative kill decision timeliness and stage gate bypass rate.

## Formula

```
PKRG = Initiatives Stopped at Gate / Initiatives Reviewed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** governance
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pmo_portfolio_governance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3403 (batch 7)
