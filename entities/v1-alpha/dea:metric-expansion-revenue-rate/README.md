# dea:metric-expansion-revenue-rate

Candidate Performance Metric record for **Expansion Revenue Rate** (ERR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-expansion-revenue-rate`
- **Name:** Expansion Revenue Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ERR

## 2. Definition

Expansion Revenue Rate (ERR) captures growth over time for organizations tracking customer success (b2b saas). Its calculation is Expansion MRR / MRR at Start of Period, measured in percent (%). It originates from and is most used in Software & SaaS practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The growth in recurring revenue from existing customers through upsell, cross-sell, and usage growth - the metric that measures whether the installed base is an appreciating asset or a depreciating one. Its strategic significance is the efficiency argument: expansion sells at a fraction of new-logo acquisition cost, through relationships that already exist, which is why a high expansion rate is the signature of a healthy product-market-flywheel and why investors reward it - net revenue retention above 100 percent means the company would grow with the sales team idle. Read the mechanism split: usage-based expansion (the product is used more), seat expansion (the account adds users), and tier expansion (the account upgrades) have different durability - usage expansion tracks product value delivered, tier expansion can be pricing-engineered, and the mix matters for how durable the rate is.

## Formula

```
Expansion MRR / MRR at Start of Period
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_success_b2b_saas
- **Sector:** software_saas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 581 (batch 2)
