# dea:metric-branch-cost-to-income-deep-dive

Candidate Performance Metric record for **Branch Cost-to-Income (Deep Dive)** (BCI-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-branch-cost-to-income-deep-dive`
- **Name:** Branch Cost-to-Income (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BCI-D

## 2. Definition

A Retail Banking Branch Network (Deep Dive) indicator, Branch Cost-to-Income (Deep Dive) (BCI-D) quantifies how efficiently resources are converted into outputs. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Branch Operating Costs / Branch Income, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Banking.

## 3. Context

Measures branch operating cost against branch-attributable income. It is the survival metric of branch networks under digital migration: each branch is a P&L with a local market, and chronic ratios above breakeven force rationalization decisions. Income attribution to branches is genuinely hard (digital-served relationships), so attribution method drives the number more than performance. Read with branch footfall to digital migration rate and market-share retention in closed-branch catchments.

## Formula

```
BCI-D = Branch Operating Costs / Branch Income
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_branch_network_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2114 (batch 6)
