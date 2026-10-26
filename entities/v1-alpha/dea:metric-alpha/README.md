# dea:metric-alpha

Candidate Performance Metric record for **Alpha** (ALPHA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-alpha`
- **Name:** Alpha
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ALPHA

## 2. Definition

Within Investment Management, Alpha (ALPHA) is used to gauge the economic value created or preserved. It is computed as Portfolio Return - Benchmark-Adjusted Expected Return, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Asset management.

## 3. Context

Alpha is the return of a portfolio above what its risk profile would predict - the intercept in a regression of portfolio returns against a benchmark, formalized in Michael Jensen's 1968 framework and now the central performance metric of the entire active management industry. Its honest reading requires nuance: alpha depends entirely on the factor model used to adjust for risk, so the same fund shows positive alpha against the S&P 500 and negative against a Fama-French three-factor model. Sample size matters too - distinguishing alpha from luck requires years of data. Read with tracking error and information ratio, and demand clarity on which model any reported alpha is measured against.

## Formula

```
Portfolio Return - Benchmark-Adjusted Expected Return
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management
- **Sector:** asset_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 762 (batch 2)
