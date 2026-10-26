# dea:metric-agency-persistency-rate

Candidate Performance Metric record for **Agency Persistency Rate** (APR-I) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-agency-persistency-rate`
- **Name:** Agency Persistency Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** APR-I

## 2. Definition

A Insurance Distribution & Agency Management indicator, Agency Persistency Rate (APR-I) quantifies the retention of customers, users, or assets over time. It is defined as Policies Renewing across Periods / Policies In Force; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Insurance, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of policies remaining in force through renewal periods, by writing agency. Persistency is the lifetime-value engine of agency-distributed insurance, and agency-level cuts expose which distribution partners write quality business versus churn-and-earn books. Watch for persistency gaps concentrated in specific products or incentive seasons, which indicate commission-driven selling. Read with agent churn rate (Insurance) and loss ratio by agency.

## Formula

```
APR-I = Policies Renewing across Periods / Policies In Force
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_agency_management
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1725 (batch 6)
