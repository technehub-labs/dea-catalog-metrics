# dea:metric-information-ratio

Candidate Performance Metric record for **Information Ratio** (IR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-information-ratio`
- **Name:** Information Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IR

## 2. Definition

Within Investment Management, Information Ratio (IR) is used to gauge the economic value created or preserved. The formula is Active Return / Tracking Error - reported in ratio (x:1 or x). It is a standard measure in the Asset management sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The information ratio is a portfolio's active return (return above benchmark) divided by the volatility of that active return - essentially a signal-to-noise measure for active management skill. An IR of 0.5 over multiple years is exceptional, and the Grinold-Kahn fundamental law of active management links it to breadth of independent bets and skill per bet. The trap is timeframe: high IR over a short window is far more likely noise than skill, and adding unrelated low-correlation positions mechanically inflates IR without adding expected return. Read alongside active share, which tells you whether the active risk is deliberate positioning or closet indexing with tracking error.

## Formula

```
Active Return / Tracking Error
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management
- **Sector:** asset_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 764 (batch 2)
