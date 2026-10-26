# dea:metric-return-on-equity

Candidate Performance Metric record for **Return on Equity** (ROE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-return-on-equity`
- **Name:** Return on Equity
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ROE

## 2. Definition

Return on Equity (ROE) captures the economic value created or preserved for organizations tracking finance & accounting. It is computed as Net Income / Shareholders' Equity, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Net income over shareholders equity - the return earned on the owners stake. It is the headline number for investors because it compounds directly into book value growth, and the DuPont decomposition (margin x turnover x leverage) exposes how the return is manufactured. That third term is the caveat: leverage manufactures ROA into ROE, so a 20 percent ROE can be a genuinely spectacular business or a modest one juiced by debt. Compare against the cost of equity rather than zero - a company earning less than its equity costs is destroying value regardless of the positive sign. Financial firms live and die by this metric; asset-light firms should expect it to run very high.

## Formula

```
Net Income / Shareholders' Equity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 12 (batch 1)
