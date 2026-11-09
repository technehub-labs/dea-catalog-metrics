# dea:metric-dividend-payout-ratio

Candidate Performance Metric record for **Dividend Payout Ratio** (DPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dividend-payout-ratio`
- **Name:** Dividend Payout Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DPR

## 2. Definition

Dividend Payout Ratio (DPR) captures the economic value created or preserved for organizations tracking investor relations & capital markets. It is computed as Dividends Paid / Net Income, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is concentrated in Listed companies.

## 3. Context

Dividends as a share of earnings - the distribution metric that encodes an entire capital-allocation philosophy in one number, and the one signaling theory interprets most sharply: payout reveals what management believes about the durability of earnings and the availability of reinvestment, because dividends are read as a commitment in a way buybacks never are. The strategic significance is the maturity story the ratio tells: growth businesses should pay little (reinvestment returns exceed what shareholders can earn elsewhere), mature cash cows should pay substantially, and the market reads a payout inconsistent with the company's reinvestment opportunities as either misallocation or distrust of its own pipeline. Read with coverage and stability: payout measured against free cash flow rather than earnings is the honest test, since dividends paid from earnings that do not convert to cash are borrowing to pay the register - and the stability dimension matters, because the signaling cost of cutting a dividend exceeds the value of ever having raised it.

## Formula

```
DPR = Dividends Paid / Net Income
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 626 (batch 2)
