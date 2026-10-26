# dea:metric-out-of-policy-spend-rate

Candidate Performance Metric record for **Out-of-Policy Spend Rate** (OPSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-out-of-policy-spend-rate`
- **Name:** Out-of-Policy Spend Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OPSR

## 2. Definition

Within Corporate Travel Management, Out-of-Policy Spend Rate (OPSR) is used to gauge conformance to standards, plans, or obligations. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Out-of-Policy Travel Spend / Total Travel Spend, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures travel spend outside policy channels and limits. It matters because leakage erodes negotiated savings and data quality. Exceptions can be pre-approved so routinely that they no longer count as out-of-policy. Read with Policy Compliance Rate (Travel) and exception approval logs to confirm leakage is genuinely falling.

## Formula

```
Out-of-Policy Travel Spend / Total Travel Spend
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_travel_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1218 (batch 4)
