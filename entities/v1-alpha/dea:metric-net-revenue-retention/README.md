# dea:metric-net-revenue-retention

Candidate Performance Metric record for **Net Revenue Retention** (NRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-revenue-retention`
- **Name:** Net Revenue Retention
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NRR

## 2. Definition

A Customer indicator, Net Revenue Retention (NRR) quantifies the retention of customers, users, or assets over time. The formula is (MRR_start + Expansion MRR - Contraction MRR - Churned MRR) / MRR_start - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

NRR (also NDR) is this period's recurring revenue from an existing cohort divided by the same cohort's revenue a year ago - including expansion, upgrades, downgrades, and churn. Above 100%, the base grows even with zero new logos; 110-120% is typical for healthy B2B SaaS, and top-decile companies exceed 130%. It is the single best summary of a subscription business's ability to grow inside its installed base, but it can mask logo churn behind expansion - always read it alongside gross retention.

## Formula

```
(MRR_start + Expansion MRR - Contraction MRR - Churned MRR) / MRR_start
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer

## Attribution

- **Source credit:** SaaS / subscription finance practice

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 72 (batch 1)
