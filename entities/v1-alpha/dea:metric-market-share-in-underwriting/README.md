# dea:metric-market-share-in-underwriting

Candidate Performance Metric record for **Market Share in Underwriting** (MSU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-market-share-in-underwriting`
- **Name:** Market Share in Underwriting
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MSU

## 2. Definition

Market Share in Underwriting (MSU) captures growth over time for organizations tracking investment banking & capital markets. It is computed as Firm Underwritten Volume / Total Market Volume, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Investment banking.

## 3. Context

Market share in underwriting measures the share of equity or debt issuance a bank books, and it is league-table logic applied to the underwriting business - share drives the perception of distribution strength, which drives future mandate selection in a self-reinforcing cycle. The strategic subtlety is share at what price: underwriting league tables can be bought by pricing aggressively (underwriting fee compression on investment-grade debt is a long industry pattern), and balance-sheet usage to win league position consumes capital. Bookrunner-share definitions (joint books split credit) mean headline share overstates true franchise position. Read with fee share versus volume share (the divergence prices the aggression), underwriting losses or buybacks of stuck deals (the true cost of share), and industry-fee-pool trend since share of a shrinking pool is not growth.

## Formula

```
Firm Underwritten Volume / Total Market Volume
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_banking_capital_markets
- **Sector:** investment_banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1150 (batch 4)
