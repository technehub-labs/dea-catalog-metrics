# dea:metric-logo-churn-rate-deep-dive

Candidate Performance Metric record for **Logo Churn Rate (Deep Dive)** (LCR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-logo-churn-rate-deep-dive`
- **Name:** Logo Churn Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LCR-D

## 2. Definition

Within Software Product Operations (Deep Dive), Logo Churn Rate (Deep Dive) (LCR-D) is used to gauge the retention of customers, users, or assets over time. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Cancelled Accounts / Total Accounts, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Technology.

## 3. Context

Measures the share of customer accounts lost, regardless of revenue weight. Logo churn is the customer-count truth beneath revenue-weighted retention: high logo churn masked by expansion revenue hides a product problem that eventually exhausts the expansion base. Segment by customer size, since SMB churn is structural while enterprise logo churn signals serious failure. Read with expansion revenue rate (SaaS Deep Dive) and churn-reason distribution.

## Formula

```
Cancelled Accounts / Total Accounts
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** software_product_operations_deep_dive
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2158 (batch 6)
