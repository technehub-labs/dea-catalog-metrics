# dea:metric-net-interest-margin

Candidate Performance Metric record for **Net Interest Margin** (NIM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-interest-margin`
- **Name:** Net Interest Margin
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NIM

## 2. Definition

A Banking & Financial Services indicator, Net Interest Margin (NIM) quantifies the economic value created or preserved. Its calculation is (Interest Income - Interest Expense) / Average Earning Assets, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Financial services practice.

## 3. Context

Net interest income as a percentage of average interest-earning assets - the fundamental profitability engine of a deposit-taking bank. It captures the spread the bank earns between lending and funding, which is the whole retail banking business model in one number. Its level is structural: Japanese banks have operated below 1 percent, US banks above 3 percent, and comparing across regimes without adjusting for rates and mix is meaningless. What management controls is the trajectory against peer set - a falling NIM usually means either funding costs are rising faster than asset yields or the mix is drifting toward lower-spread assets. Analysts watch it alongside loan growth: chasing NIM by reaching for credit risk is the classic way this metric kills a bank.

## Formula

```
(Interest Income - Interest Expense) / Average Earning Assets
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
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 35 (batch 1)
