# dea:metric-best-execution-compliance-rate

Candidate Performance Metric record for **Best Execution Compliance Rate** (BECR-IM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-best-execution-compliance-rate`
- **Name:** Best Execution Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BECR-IM

## 2. Definition

Best Execution Compliance Rate (BECR-IM) captures conformance to standards, plans, or obligations for organizations tracking investment management - portfolio operations. Its calculation is Trades Meeting Best Execution Policy / Sampled, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Financial Services practice.

## 3. Context

Measures adherence to best-execution obligations across venue, price, and cost dimensions. It is a core regulatory duty where process failures become enforcement matters. Compliance measured as documented process rather than measured outcomes is increasingly challenged. Read with transaction cost analysis and trade error rate.

## Formula

```
BECR-IM = Trades Meeting Best Execution Policy / Sampled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3016 (batch 7)
