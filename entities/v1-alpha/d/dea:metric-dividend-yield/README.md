# dea:metric-dividend-yield

Candidate Performance Metric record for **Dividend Yield** (DIVY) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dividend-yield`
- **Name:** Dividend Yield
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DIVY

## 2. Definition

Dividend Yield (DIVY) captures the economic value created or preserved for organizations tracking investor relations & capital markets. It is defined as Annual Dividend per Share / Share Price; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. In Listed companies, it is a recognized element of the standard performance toolkit.

## 3. Context

Annual dividends per share divided by price - the return metric that frames equity income, and the number that anchors a whole investment style: income investors screen on it, total-return comparisons contextualize against it, and the yield-versus-bond-yield comparison has been a market-level valuation signal since before the equity-risk-premium literature formalized it. The strategic significance for the issuer is register-shaping: a meaningful yield attracts a stable, income-oriented holder base that behaves differently from momentum holders - steadier in drawdowns, less price-sensitive in rallies - and that register composition is a deliberate result companies can cultivate. The trap the metric invites is yield-chasing: an unusually high yield is usually the market pricing a cut - yield rises mechanically as price falls on deterioration - so the metric is always read with payout sustainability, coverage, and the balance sheet behind the distribution.

## Formula

```
DIVY = Annual Dividend per Share / Share Price
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investor_relations_capital_markets
- **Sector:** listed_companies

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 627 (batch 2)
