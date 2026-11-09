# dea:metric-risk-adjusted-approval-rate

Candidate Performance Metric record for **Risk-Adjusted Approval Rate** (RAAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-risk-adjusted-approval-rate`
- **Name:** Risk-Adjusted Approval Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RAAR

## 2. Definition

A Credit & Collections Risk (Enterprise) indicator, Risk-Adjusted Approval Rate (RAAR) quantifies conformance to standards, plans, or obligations. Its calculation is Approvals within Risk Appetite / Approvals, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures approval decisions adjusted for the risk level of applicants. It separates a genuinely expanding book from a loosening one. Risk adjustment built on the approval model's own scores is circular. Read with probability of default (Deep Dive) and vintage default emergence curve.

## Formula

```
RAAR = Approvals within Risk Appetite / Approvals
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** credit_collections_risk_enterprise

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4210 (batch 9)
