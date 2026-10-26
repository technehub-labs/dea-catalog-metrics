# dea:metric-underwriting-profit-margin-deep-dive

Candidate Performance Metric record for **Underwriting Profit Margin (Deep Dive)** (UWPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-underwriting-profit-margin-deep-dive`
- **Name:** Underwriting Profit Margin (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** UWPM

## 2. Definition

Underwriting Profit Margin (Deep Dive) (UWPM) addresses the economic value created or preserved and is a fixture of insurance underwriting reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is (Earned Premium - Claims - Expenses) / Earned Premium - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Insurance sector.

## 3. Context

Measures underwriting profit - earned premium minus losses, expenses, and reinsurance costs - as a margin, the underwriting-only view stripping investment income. It matters because insurers can look profitable while underwriting unprofitably, sustained only by float returns, and that structure is fragile in rate-cut environments. Allocate reinsurance and expense honestly at segment level or the deep dive becomes a blended blur. Read with combined ratio components and reserve development for delayed reality.

## Formula

```
(Earned Premium - Claims - Expenses) / Earned Premium
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
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1506 (batch 6)
