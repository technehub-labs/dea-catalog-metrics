# dea:metric-risk-appetite-relevance-rate

Candidate Performance Metric record for **Risk Appetite Relevance Rate** (RAR-ER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-risk-appetite-relevance-rate`
- **Name:** Risk Appetite Relevance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RAR-ER

## 2. Definition

Risk Appetite Relevance Rate (RAR-ER) measures conformance to standards, plans, or obligations in the Emerging Risk & Horizon Scanning domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Appetite Statements Confirmed Current at Review / Statements; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether the stated appetite statement covers the risks the organization actually faces today. Appetite statements written years ago silently become fiction. Relevance scored by the statement's authors grades its own homework. Read with risk appetite threshold utilization and risk appetite statement effectiveness.

## Formula

```
RAR-ER = Appetite Statements Confirmed Current at Review / Statements
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
- **Domain:** emerging_risk_horizon_scanning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4002 (batch 8)
