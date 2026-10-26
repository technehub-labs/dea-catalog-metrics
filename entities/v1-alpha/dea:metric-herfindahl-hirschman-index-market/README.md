# dea:metric-herfindahl-hirschman-index-market

Candidate Performance Metric record for **Herfindahl-Hirschman Index (Market)** (HHI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-herfindahl-hirschman-index-market`
- **Name:** Herfindahl-Hirschman Index (Market)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** HHI

## 2. Definition

A Market Structure & Economics Standard Measures indicator, Herfindahl-Hirschman Index (Market) (HHI) quantifies exposure to adverse outcomes. It is computed as Sum of Squared Market Shares of Competitors, expressed in index (0-100 or normalized). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The HHI sums the squared market shares of all competitors, producing a concentration measure from near 0 (atomistic) to 10,000 (monopoly). Antitrust practice treats markets above 2,500 as highly concentrated, 1,500-2,500 moderately - the thresholds the US merger guidelines use to flag deals for scrutiny. Squaring means large firms dominate the index: a merger of two 30% players moves HHI by 1,800 points, two 5% players by 50. Its sensitivity is market definition - draw the market narrowly and everything looks concentrated - so always state the market boundary used.

## Formula

```
Sum of Squared Market Shares of Competitors
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** risk
- **Scope classification:** business_domain
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** market_structure_economics_standard_measures

## Attribution

- **Source credit:** Orris C. Herfindahl / Albert O. Hirschman

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4135 (batch 9)
