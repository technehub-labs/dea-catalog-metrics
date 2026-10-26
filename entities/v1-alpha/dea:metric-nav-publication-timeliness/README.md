# dea:metric-nav-publication-timeliness

Candidate Performance Metric record for **NAV Publication Timeliness** (NAVPT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-nav-publication-timeliness`
- **Name:** NAV Publication Timeliness
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NAVPT

## 2. Definition

A Investment Management - Portfolio Operations indicator, NAV Publication Timeliness (NAVPT) quantifies conformance to standards, plans, or obligations. It is computed as NAVs Published within Commitment / Publications, expressed in percent (%). Its use is concentrated in Financial Services. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether NAVs are published within required deadlines. Timely NAV is a fund-operations SLA: late NAVs cascade into client reporting and dealing failures. Persistent lateness usually signals upstream data-vendor or pricing issues, not effort. Read with NAV calculation accuracy rate and client reporting accuracy rate.

## Formula

```
NAVs Published within Commitment / Publications
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3013 (batch 7)
