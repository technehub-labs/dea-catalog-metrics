# dea:metric-magic-number-deep-dive

Candidate Performance Metric record for **Magic Number (Deep Dive)** (MN-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-magic-number-deep-dive`
- **Name:** Magic Number (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MN-D

## 2. Definition

Magic Number (Deep Dive) (MN-D) measures how efficiently resources are converted into outputs in the Startup & Venture-Backed Business domain. Its calculation is Net New ARR Quarter / Prior Quarter Sales and Marketing Spend, measured in ratio (x:1 or x). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The SaaS magic number is the quarter's net new ARR divided by the prior quarter's sales and marketing spend - the payback-oriented efficiency test from Bessemer-style benchmarking. A magic number of 0.75 means each sales dollar returns 75 cents of new ARR within the quarter; above 1.0 argues for aggressive go-to-market spend, below 0.5 for fixing the funnel before spending more. Its famous use is the invest-or-fix decision, and its limits are that it is trailing, quarterly-noisy, and blind to payback period and churn.

## Formula

```
Net New ARR Quarter / Prior Quarter Sales and Marketing Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** startup_venture_backed_business

## Attribution

- **Source credit:** SaaS growth benchmarking practice (Bessemer tradition)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2445 (batch 6)
