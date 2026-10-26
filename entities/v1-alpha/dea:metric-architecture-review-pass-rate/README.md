# dea:metric-architecture-review-pass-rate

Candidate Performance Metric record for **Architecture Review Pass Rate** (ARPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-architecture-review-pass-rate`
- **Name:** Architecture Review Pass Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ARPR

## 2. Definition

A Enterprise Architecture indicator, Architecture Review Pass Rate (ARPR) quantifies the quality of outputs and outcomes. It is defined as Designs Approved at First Review / Designs Reviewed; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of designs passing architecture reviews without major rework. It matters because reviews are the quality gate preventing architectural debt accumulation. Reviews can become rubber stamps under delivery pressure. Read with Production Incident causes traced to design and Technical Debt backlog trends to confirm reviews hold the line.

## Formula

```
ARPR = Designs Approved at First Review / Designs Reviewed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** enterprise_architecture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1347 (batch 5)
