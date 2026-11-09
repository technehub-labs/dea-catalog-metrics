# dea:metric-gross-profit-margin

Candidate Performance Metric record for **Gross Profit Margin** (GPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gross-profit-margin`
- **Name:** Gross Profit Margin
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GPM

## 2. Definition

Gross Profit Margin (GPM) measures the economic value created or preserved in the Finance & Accounting domain. It is computed as (Revenue - Cost of Goods Sold) / Revenue, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The most basic test of whether a business has a viable product economics: revenue minus cost of goods sold, as a share of revenue. It measures pricing power and production efficiency before any overhead is counted, which is why small movements matter - a two-point gross margin decline that looks minor at the top line can halve what is left for operating expenses. Analysts read it against industry peers rather than absolute levels, since software (often above 70 percent) and grocery retail (often below 25 percent) are healthy at wildly different numbers. Watch the accounting: inventory method and what is classified into COGS both move this metric without any real change in the business.

## Formula

```
GPM = (Revenue - Cost of Goods Sold) / Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 7 (batch 1)
