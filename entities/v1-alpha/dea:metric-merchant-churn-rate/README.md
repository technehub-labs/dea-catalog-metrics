# dea:metric-merchant-churn-rate

Candidate Performance Metric record for **Merchant Churn Rate** (MCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-merchant-churn-rate`
- **Name:** Merchant Churn Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MCR

## 2. Definition

Merchant Churn Rate (MCR) addresses exposure to adverse outcomes and is a fixture of payments & fintech reporting. It is defined as Merchants Lost / Merchants at Start of Period; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. In Payments & fintech, it is a recognized element of the standard performance toolkit.

## 3. Context

Merchant churn measures the share of merchants (by count or volume) terminating processing relationships, and it is the retention counterpart of the payments industry's growth engine. Churn here has distinctive structure: merchants fail for business reasons (small-business mortality is high), get acquired, or churn voluntarily over pricing - and each type responds to different interventions, so the blended rate is a weak management signal. Volume-weighted churn matters more than count churn because payments economics are volume-concentrated: the top 1 percent of merchants can be a third of volume. Read with cohort-based retention by merchant segment, pricing-tier migration, and volume decline preceding churn (merchants usually fade before they formally terminate).

## Formula

```
MCR = Merchants Lost / Merchants at Start of Period
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** payments_fintech
- **Sector:** payments_fintech

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 784 (batch 2)
