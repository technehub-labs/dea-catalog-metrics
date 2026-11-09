# dea:metric-net-profit-margin

Candidate Performance Metric record for **Net Profit Margin** (NPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-profit-margin`
- **Name:** Net Profit Margin
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NPM

## 2. Definition

Net Profit Margin (NPM) captures the economic value created or preserved for organizations tracking finance & accounting. The formula is Net Income / Revenue - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The bottom line as a share of the top line - net income divided by revenue. It is the fullest measure of overall profitability because it absorbs everything: production costs, operating expenses, interest burden, tax, and one-off items. That completeness is also its weakness, since a single write-down or tax credit can swing it without any change in underlying trading. Strategic readers decompose it rather than take it at face value - gross margin times operating efficiency times financing and tax effects - and compare the decomposition, not just the total. A stable net margin built on falling gross margin is a warning, not a comfort.

## Formula

```
NPM = Net Income / Revenue
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 9 (batch 1)
