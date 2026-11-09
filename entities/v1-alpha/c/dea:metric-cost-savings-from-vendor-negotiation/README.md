# dea:metric-cost-savings-from-vendor-negotiation

Candidate Performance Metric record for **Cost Savings from Vendor Negotiation** (CSVN) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-savings-from-vendor-negotiation`
- **Name:** Cost Savings from Vendor Negotiation
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CSVN

## 2. Definition

Cost Savings from Vendor Negotiation (CSVN) addresses the economic value created or preserved and is a fixture of outsourcing & vendor management reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Negotiated Reduction vs Initial Quote, Annualized, measured in currency value. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Cost savings from vendor negotiation measures spend reduction captured through sourcing and negotiation activity, and it is the procurement function's headline value metric - the number that justifies procurement's existence and budget. The honesty challenge is baseline-definition: savings against list price are worth less than savings against last-year's price, and first-time-sourced spend and renewal spend produce savings with different durability. The gaming risk is category-shifting: savings claimed through specification reduction (less service, lower quality, worse terms) are not savings but value transfer from quality to price. The financial-validation discipline matters as much as for improvement projects: savings only count when they appear in the budget. Read with budget-variance reconciliation (validated savings versus claimed), contract-term quality (savings that trade away flexibility cost more later), and spend-under-management growth which is procurement's scope metric.

## Formula

```
CSVN = Negotiated Reduction vs Initial Quote, Annualized
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** outsourcing_vendor_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1127 (batch 4)
