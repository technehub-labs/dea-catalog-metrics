# dea:metric-cross-border-payment-cost-ratio

Candidate Performance Metric record for **Cross-Border Payment Cost Ratio** (CBPCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cross-border-payment-cost-ratio`
- **Name:** Cross-Border Payment Cost Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CBPCR

## 2. Definition

A Payments & Cards (Deep Dive) indicator, Cross-Border Payment Cost Ratio (CBPCR) quantifies how efficiently resources are converted into outputs. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Total Cost of Cross-Border Payment / Value, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Payments practice.

## 3. Context

Measures the total cost of international payments - FX spread, correspondent fees, scheme fees - against transfer volume. Cross-border corridors carry stubbornly high friction costs, and transparency regulation has pushed the all-in cost into the light, making this both a compliance-disclosure and a competitiveness metric. All-in cost must include the FX spread, or the number is fiction. Read with corridor-level speed and failure rates and settlement risk exposure.

## Formula

```
Total Cost of Cross-Border Payment / Value
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** payments_cards_deep_dive
- **Sector:** payments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2099 (batch 6)
