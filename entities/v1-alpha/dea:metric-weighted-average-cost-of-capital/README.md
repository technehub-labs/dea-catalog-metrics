# dea:metric-weighted-average-cost-of-capital

Candidate Performance Metric record for **Weighted Average Cost of Capital** (WACC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-weighted-average-cost-of-capital`
- **Name:** Weighted Average Cost of Capital
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WACC

## 2. Definition

Weighted Average Cost of Capital (WACC) captures the economic value created or preserved for organizations tracking treasury & cash management. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Weighted Average of Cost of Equity and After-Tax Cost of Debt, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The blended required return on all capital - the cost of equity from the capital-asset-pricing tradition plus the after-tax cost of debt, weighted by market-value proportions - the single most consequential rate in corporate finance. Its strategic significance is threshold-setting: it is the hurdle every investment must clear, the discount rate every DCF uses, and the number against which ROIC is compared to determine whether value is created - so the entire capital-allocation process is arbitrated by it. The estimation humility matters: the equity leg rests on the beta and equity-risk-premium assumptions, and reasonable practitioners disagree by percentage points, which moves valuations enormously - so mature organizations test decisions against a WACC range rather than a point. Read with the financing-reality check: the computed WACC assumes financing at current market terms, and a firm whose actual capital structure deviates from the optimal one is paying a different rate in practice than the model says.

## Formula

```
Weighted Average of Cost of Equity and After-Tax Cost of Debt
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** treasury_cash_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 595 (batch 2)
