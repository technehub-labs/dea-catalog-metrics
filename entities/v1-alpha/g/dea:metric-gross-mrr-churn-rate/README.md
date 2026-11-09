# dea:metric-gross-mrr-churn-rate

Candidate Performance Metric record for **Gross MRR Churn Rate** (GMChurn) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gross-mrr-churn-rate`
- **Name:** Gross MRR Churn Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GMChurn

## 2. Definition

Gross MRR Churn Rate (GMChurn) addresses the retention of customers, users, or assets over time and is a fixture of customer success (b2b saas) reporting. The formula is Churned MRR / MRR at Start of Period - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Software & SaaS sector.

## 3. Context

Recurring revenue lost from the existing base in a month, excluding expansion - the leak-rate metric of subscription economics, measuring contraction and cancellation without the compensation of upsell. Its strategic significance is the floor it sets: whatever growth the sales motion produces, this rate subtracts, and at scale the arithmetic dominates - a monthly gross churn of 2 percent means a quarter of the base evaporates annually before new sales add anything. The honest separation from net churn is the whole point: net MRR churn can look healthy while gross churn deteriorates, meaning expansion is outrunning a widening leak, a state that holds only until the expansion pool thins. Read the split between logo loss and contraction: customers leaving (product-fit problem) and customers downgrading (value-delivery problem) are different failures with different remedies, and the blended rate hides which is growing.

## Formula

```
GMChurn = Churned MRR / MRR at Start of Period
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_success_b2b_saas
- **Sector:** software_saas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 578 (batch 2)
