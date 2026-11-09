# dea:metric-price-realization-rate

Candidate Performance Metric record for **Price Realization Rate** (PRR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-price-realization-rate`
- **Name:** Price Realization Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PRR-P

## 2. Definition

Price Realization Rate (PRR-P) measures the economic value created or preserved in the Pricing & Revenue Management domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Actual Average Selling Price / List or Target Price, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Price realization rate measures the share of list-price or target-price increases actually captured in invoiced revenue, and it is the pricing-discipline metric that closes the gap between pricing strategy and pricing reality - most companies believe their prices are their published rates, but discounting, ad-hoc concessions, and deal-desk overrides erode them invisibly. The metric is the antidote to the classic pricing failure mode: the pricing team sets strategy while the sales team executes whatever the deal needs, and neither sees the gap. Realization decomposition is the management information: standard discount (planned) versus discretionary discount (judgment) versus leakage (unapproved) each need different fixes - the first is strategy, the second is governance, the third is control failure. Read with discount-leakage trend, deal-level realization distribution (averages hide bimodal outcomes), and realization by salesperson to identify training versus policy issues.

## Formula

```
PRR-P = Actual Average Selling Price / List or Target Price
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pricing_revenue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1064 (batch 4)
