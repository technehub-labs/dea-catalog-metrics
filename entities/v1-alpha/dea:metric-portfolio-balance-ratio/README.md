# dea:metric-portfolio-balance-ratio

Candidate Performance Metric record for **Portfolio Balance Ratio** (PBR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-portfolio-balance-ratio`
- **Name:** Portfolio Balance Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PBR

## 2. Definition

Portfolio Balance Ratio (PBR) captures the economic value created or preserved for organizations tracking strategy & portfolio. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Growth Investment / Maintenance Investment - reported in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The distribution of the portfolio across intended categories - conventionally the share of investment or resources allocated to each strategic bucket, compared against the intended balance (for instance the horizon model of near, mid, and far bets, or the run-grow-transform split). Its strategic weight is the drift it exposes: every large organization's intended portfolio skews toward near-term, low-risk work over time, because incremental requests crowd out exploratory ones, and this metric is the early-warning gauge of that drift. The measurement question is what counts - initiatives counted by number underweights the few big bets that carry the future, so the ratio is computed on investment spend, with a floor rule that prevents counting many small projects as portfolio diversification. Read annually against the strategy's stated intent, which is what the ratio is balanced against.

## Formula

```
Growth Investment / Maintenance Investment
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** strategy_portfolio

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 369 (batch 1)
