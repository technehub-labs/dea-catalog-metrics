# dea:metric-retention-ratio-earnings

Candidate Performance Metric record for **Retention Ratio (Earnings)** (RRE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-retention-ratio-earnings`
- **Name:** Retention Ratio (Earnings)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RRE

## 2. Definition

Retention Ratio (Earnings) (RRE) measures the economic value created or preserved in the Valuation & Corporate Finance Standard Measures domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Retained Earnings / Net Income - reported in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of earnings retained for reinvestment. Retention funds growth; its value depends on the returns reinvestment earns. High retention with low ROIC is value destruction retained. Read with dividend payout ratio (Deep Dive) and sustainable growth rate.

## Formula

```
RRE = Retained Earnings / Net Income
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** valuation_corporate_finance_standard_measures

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4047 (batch 9)
