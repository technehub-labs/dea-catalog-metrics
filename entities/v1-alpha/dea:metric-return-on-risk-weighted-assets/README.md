# dea:metric-return-on-risk-weighted-assets

Candidate Performance Metric record for **Return on Risk-Weighted Assets** (RORWA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-return-on-risk-weighted-assets`
- **Name:** Return on Risk-Weighted Assets
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RORWA

## 2. Definition

Return on Risk-Weighted Assets (RORWA) measures the economic value created or preserved in the Banking & Financial Services domain. The formula is Net Income / Risk-Weighted Assets - reported in percent (%). It is a standard measure in the Financial services sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Profitability divided not by balance-sheet size but by risk-weighted assets - the metric through which banks increasingly steer capital allocation, because RWA is the true scarce resource in a Basel-regulated institution. Two divisions with identical profit can earn very different RoRWA depending on the risk weights their books attract, which redirects capital toward businesses that earn well per unit of regulatory risk - a strategically more honest measure than return on equity, which ignores risk entirely. It is the decomposition input of choice for bank equity stories: RWA density times leverage times RoRWA rebuilds the ROE, showing whether returns come from efficient use of capital or from leverage on it.

## Formula

```
Net Income / Risk-Weighted Assets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 44 (batch 1)
