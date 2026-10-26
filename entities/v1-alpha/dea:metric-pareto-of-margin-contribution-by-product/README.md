# dea:metric-pareto-of-margin-contribution-by-product

Candidate Performance Metric record for **Pareto of Margin Contribution by Product** (PMCP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pareto-of-margin-contribution-by-product`
- **Name:** Pareto of Margin Contribution by Product
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PMCP

## 2. Definition

Pareto of Margin Contribution by Product (PMCP) captures the economic value created or preserved for organizations tracking pricing & revenue management. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Margin from Top Products / Total Margin; the result is stated in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The Pareto of margin contribution ranks products by their share of total margin, and it is the portfolio-truth metric of pricing analysis - margin concentration (a small share of products generating most margin) is the norm, not the exception, and the distribution determines which products deserve pricing attention, engineering investment, and sales focus. The strategic insight is that revenue rankings and margin rankings diverge dramatically: high-volume, low-margin products can dominate revenue while a handful of specialty products carry the actual profit, so resource allocation driven by revenue misallocates. The tail analysis is where action lives: loss-making products at the tail should be repriced, re-costed, or killed, and the refusal to prune the tail is a common strategic failure. Read with revenue-versus-margin rank divergence, product lifecycle position (tail products may be early-stage or declining), and cross-subsidy effects where high-margin products fund strategic ones.

## Formula

```
Margin from Top Products / Total Margin
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Domain:** pricing_revenue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1074 (batch 4)
