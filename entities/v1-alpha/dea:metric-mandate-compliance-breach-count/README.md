# dea:metric-mandate-compliance-breach-count

Candidate Performance Metric record for **Mandate Compliance Breach Count** (MCBC-IM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mandate-compliance-breach-count`
- **Name:** Mandate Compliance Breach Count
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MCBC-IM

## 2. Definition

Within Investment Management - Portfolio Operations, Mandate Compliance Breach Count (MCBC-IM) is used to gauge conformance to standards, plans, or obligations. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Investment Guideline Breaches per Period, measured in count (items per period). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Financial Services practice.

## 3. Context

Measures breaches of investment guidelines and client mandates. Breaches are fiduciary and often contractual failures carrying regulatory notification duties. Counting only breaches unresolved at period end hides those fixed quietly. Read with guideline pre-trade compliance coverage and asset allocation drift ratio.

## Formula

```
Investment Guideline Breaches per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3026 (batch 7)
