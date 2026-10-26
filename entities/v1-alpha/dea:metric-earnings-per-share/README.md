# dea:metric-earnings-per-share

Candidate Performance Metric record for **Earnings per Share** (EPS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-earnings-per-share`
- **Name:** Earnings per Share
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EPS

## 2. Definition

Earnings per Share (EPS) measures the economic value created or preserved in the Finance & Accounting domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is (Net Income - Preferred Dividends) / Weighted Average Shares Outstanding, measured in currency value. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Net income attributable to common shareholders divided by shares outstanding - the per-share distillation of profit that anchors price-to-earnings valuation and dividend policy. Its usefulness comes from being the arithmetic bridge between company performance and shareholder return, but that closeness to markets is also its weakness: buybacks shrink the denominator and lift EPS without any operating improvement, a trick so common that EPS growth must be checked against net income growth before crediting management. Diluted share counts - including options and convertibles - are the honest denominator, and the basic-versus-diluted gap measures the transfer of value to option holders.

## Formula

```
(Net Income - Preferred Dividends) / Weighted Average Shares Outstanding
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 28 (batch 1)
