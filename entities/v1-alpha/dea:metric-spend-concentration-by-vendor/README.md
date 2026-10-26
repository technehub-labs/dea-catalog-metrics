# dea:metric-spend-concentration-by-vendor

Candidate Performance Metric record for **Spend Concentration by Vendor** (SCV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-spend-concentration-by-vendor`
- **Name:** Spend Concentration by Vendor
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SCV

## 2. Definition

Spend Concentration by Vendor (SCV) measures exposure to adverse outcomes in the Outsourcing & Vendor Management domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Largest Vendor Spend / Total Outsourced Spend; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Spend concentration by vendor measures the share of total spend going to the largest vendors - the portfolio-risk metric of procurement - and it is the tension metric of the build-versus-buy-versus-diversify question: concentration earns scale pricing and deep integration but creates dependency, exit cost, and negotiation asymmetry that compounds over time. The measurement goes beyond top-vendor share: concentration within single-vendor-dependency categories (a vendor that is 3 percent of total spend but the sole provider of a critical service is concentrated where it matters), geographic concentration, and sub-tier dependency concentration all quantify different failure modes. The strategic question is deliberate: some concentration is correct economics, some is legacy accident, and the metric's job is to make the choice visible. Read with exit-plan coverage for concentrated vendors, single-source dependency inventory, and pricing-versus-market benchmarking which reveals when concentration is being exploited.

## Formula

```
Largest Vendor Spend / Total Outsourced Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** outsourcing_vendor_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1130 (batch 4)
