# dea:metric-cost-of-poor-quality

Candidate Performance Metric record for **Cost of Poor Quality** (COPQ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-of-poor-quality`
- **Name:** Cost of Poor Quality
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** COPQ

## 2. Definition

Cost of Poor Quality (COPQ) measures the economic value created or preserved in the Quality Management domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Internal Failure + External Failure + Appraisal + Prevention Costs - reported in currency value. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The total cost of failing to do things right the first time - prevention and appraisal costs excluded, failure costs included: scrap, rework, warranty, returns, inspection of suspect product, and the harder-to-trace costs of lost sales from quality reputation. Its strategic power is magnitude: quality practitioners from Juran onward argued that this typically runs a surprising double-digit share of revenue, which reframes quality from a technical program to one of the largest cost lines a company has. Making it visible converts quality from a moral argument to a capital-allocation one - a prevention dollar that removes multiple failure dollars is a return no other cost program reliably offers. The measurement is genuinely hard, since external failure costs - the customers who quietly did not come back - never appear on any invoice.

## Formula

```
Internal Failure + External Failure + Appraisal + Prevention Costs
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** capability
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 235 (batch 1)
