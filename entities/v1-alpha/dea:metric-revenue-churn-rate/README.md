# dea:metric-revenue-churn-rate

Candidate Performance Metric record for **Revenue Churn Rate** (RevChurn) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-churn-rate`
- **Name:** Revenue Churn Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RevChurn

## 2. Definition

Revenue Churn Rate (RevChurn) addresses exposure to adverse outcomes and is a fixture of customer reporting. It is defined as (MRR_start - MRR_end + Upgrade MRR) / MRR_start; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The revenue lost from existing customers over a period - the economic refinement of logo churn, because it weighs customers by what they pay and captures the quiet killer that logo churn misses: contractions, downgrades, and negotiated discounts that keep the logo but shrink the wallet. In B2B SaaS it is read with its mirror, net revenue retention: gross churn minus expansion, where a NRR above 100 percent means the existing base grows with zero sales hires. The strategic use is demand-quality diagnosis - revenue churn driven by failed outcomes shows up in support and usage data months before the renewal date, which is what makes it actionable rather than merely descriptive.

## Formula

```
(MRR_start - MRR_end + Upgrade MRR) / MRR_start
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 71 (batch 1)
