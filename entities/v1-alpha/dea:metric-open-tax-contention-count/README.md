# dea:metric-open-tax-contention-count

Candidate Performance Metric record for **Open Tax Contention Count** (OTCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-open-tax-contention-count`
- **Name:** Open Tax Contention Count
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OTCC

## 2. Definition

Open Tax Contention Count (OTCC) captures exposure to adverse outcomes for organizations tracking tax & fiscal. Its calculation is Unresolved Tax Disputes with Authorities, measured in count (items per period). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The number of unresolved tax disputes and open examinations - the exposure metric of the tax controversy portfolio, whose strategic significance is cash-timing and provision economics: each open matter carries a potential payment, an interest clock in most regimes, and a provision question, and the count by materiality is the ledger finance teams use to model the range of outcomes. The honest read is weighted by exposure and stage: a hundred routine open items in early correspondence are a workload, one transfer-pricing dispute at the appeal stage is a material-uncertainty event, and the count alone conflates the two - so the metric is always read with the provision-relevant subset called out. Read with the aging: matters aging past the fast-resolution window statistically resolve worse, so the aging distribution is the trend within the trend.

## Formula

```
Unresolved Tax Disputes with Authorities
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** tax_fiscal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 609 (batch 2)
