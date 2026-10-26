# dea:metric-saas-quick-ratio-deep-dive

Candidate Performance Metric record for **SaaS Quick Ratio (Deep Dive)** (SAQRD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-saas-quick-ratio-deep-dive`
- **Name:** SaaS Quick Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SAQRD

## 2. Definition

SaaS Quick Ratio (Deep Dive) (SAQRD) captures growth over time for organizations tracking unit economics & growth (deep dive). Its calculation is (New + Expansion MRR) / (Churned + Contraction MRR), measured in ratio (x:1 or x). It originates from and is most used in Software practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures new plus expansion revenue divided by churned revenue. Above 1 means growth; the multiple shows how efficiently. The ratio ignores cost and margin entirely: fast can be unprofitable. Read with net dollar retention (Deep Dive) and gross dollar retention (Deep Dive).

## Formula

```
(New + Expansion MRR) / (Churned + Contraction MRR)
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** growth
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** unit_economics_growth_deep_dive
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4159 (batch 9)
