# dea:metric-gross-revenue-retention

Candidate Performance Metric record for **Gross Revenue Retention** (GRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gross-revenue-retention`
- **Name:** Gross Revenue Retention
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GRR

## 2. Definition

Within Sales, Gross Revenue Retention (GRR) is used to gauge the retention of customers, users, or assets over time. It is computed as (MRR_start - Churned MRR) / MRR_start, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of beginning-period recurring revenue retained at period end, excluding all expansion - the metric that isolates the leak in the bucket before any upsell water is poured in. A GRR of 90 percent means the base decays 10 percent annually no matter how impressive net retention looks on top of it, and that decay rate is structural: it reflects product-market fit at renewal, not sales effort. Strategically it is the floor beneath net revenue retention - NRR can exceed 100 percent while GRR quietly falls, meaning expansion is merely outrunning a worsening leak, which holds until expansion saturates. Investors increasingly ask for both numbers precisely because GRR cannot be dressed up by upsell.

## Formula

```
(MRR_start - Churned MRR) / MRR_start
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 102 (batch 1)
