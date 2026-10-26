# dea:metric-alliance-margin-contribution

Candidate Performance Metric record for **Alliance Margin Contribution** (AMC-AP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-alliance-margin-contribution`
- **Name:** Alliance Margin Contribution
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AMC-AP

## 2. Definition

A Alliances & Partnerships Management indicator, Alliance Margin Contribution (AMC-AP) quantifies the economic value created or preserved. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Alliance Gross Margin / Total Gross Margin, measured in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the profit, not just revenue, attributable to alliance-sourced business. Margin separates valuable partnerships from revenue-dilutive ones. Margins computed before allocated partnership overhead overstate. Read with partnership revenue contribution and cost-to-serve per partner.

## Formula

```
AMC-AP = Alliance Gross Margin / Total Gross Margin
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** alliances_partnerships_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3971 (batch 8)
