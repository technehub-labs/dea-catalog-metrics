# dea:metric-net-operating-income-per-asset

Candidate Performance Metric record for **Net Operating Income per Asset** (NOIA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-operating-income-per-asset`
- **Name:** Net Operating Income per Asset
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NOIA

## 2. Definition

Net Operating Income per Asset (NOIA) measures the economic value created or preserved in the Facilities & Real Estate domain. It is defined as Property Revenue - Property Operating Expenses; the result is stated in currency value. It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Property revenue minus property operating expenses - the per-asset form of the income metric that everything in real-estate valuation ultimately capitalizes. Its strategic significance is the asset-level truth it forces: portfolio averages hide the assets that drag, and per-asset NOI makes the bottom of the portfolio visible for exactly the decisions that matter - hold, reposition, or sell. Read the trend per asset rather than the level: an asset whose NOI is eroding under flat rents and rising expenses is deteriorating invisibly, and the expense-splitting (controllable versus non-controllable, especially property taxes) shows whether decline is management or market. The metric's power is its decomposition-structure: revenue, occupancy, and expenses are all individually actionable, and the movement of NOI identifies which of the three the asset strategy should attack.

## Formula

```
NOIA = Property Revenue - Property Operating Expenses
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
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facilities_real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 457 (batch 1)
