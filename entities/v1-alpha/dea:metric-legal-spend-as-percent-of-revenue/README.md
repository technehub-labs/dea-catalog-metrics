# dea:metric-legal-spend-as-percent-of-revenue

Candidate Performance Metric record for **Legal Spend as Percent of Revenue** (LSPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-legal-spend-as-percent-of-revenue`
- **Name:** Legal Spend as Percent of Revenue
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LSPR

## 2. Definition

Legal Spend as Percent of Revenue (LSPR) measures how efficiently resources are converted into outputs in the Legal Operations domain. The formula is Total Legal Spend / Revenue - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures total legal department and outside counsel spend against revenue. It benchmarks the cost of legal protection across firms, and outliers in either direction indicate risk appetite problems, not just efficiency. Be careful with litigation-driven volatility: multi-year matters distort annual ratios, so normalize with reserve and matter-cycle context. Read with matter mix, outside counsel rate realizations, and litigation outcomes.

## Formula

```
LSPR = Total Legal Spend / Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** legal_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1671 (batch 6)
