# dea:metric-institutional-ownership-share

Candidate Performance Metric record for **Institutional Ownership Share** (IOS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-institutional-ownership-share`
- **Name:** Institutional Ownership Share
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** IOS

## 2. Definition

Institutional Ownership Share (IOS) captures the economic value created or preserved for organizations tracking investor relations & capital markets. Its calculation is Institutionally Held Shares / Shares Outstanding, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. It originates from and is most used in Listed companies practice.

## 3. Context

The proportion of shares held by institutional investors - the ownership-structure metric that both predicts and constrains: institutions bring the liquidity, research attention, and voting discipline that professionalize a register, and they bring the ownership concentration that makes governance campaigns and activist attention feasible at all. Its strategic significance is register-reading: the mix between long-only funds, index money, and activist-adjacent ownership describes what kind of pressure the board should expect, and shifts in the institutional mix routinely precede governance events - which is why IR teams monitor the register by holder type, not just the total. Read with the turnover dimension: passive index ownership is stable and unresponsive, active ownership is responsive and opinionated, and the same institutional share built from one or the other is a fundamentally different register to manage.

## Formula

```
Institutionally Held Shares / Shares Outstanding
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
- **Domain:** investor_relations_capital_markets
- **Sector:** listed_companies

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 624 (batch 2)
