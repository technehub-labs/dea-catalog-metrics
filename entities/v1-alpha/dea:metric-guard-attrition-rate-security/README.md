# dea:metric-guard-attrition-rate-security

Candidate Performance Metric record for **Guard Attrition Rate (Security)** (GAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-guard-attrition-rate-security`
- **Name:** Guard Attrition Rate (Security)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GAR

## 2. Definition

A Security Services & Guarding indicator, Guard Attrition Rate (Security) (GAR) quantifies the retention of customers, users, or assets over time. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Guards Leaving / Guards Employed, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Security.

## 3. Context

Measures security officer turnover. Guarding is a low-margin, high-turnover industry, and attrition is the dominant cost driver: every lost guard carries recruiting, training, vetting, and site-knowledge costs, and service continuity failures are the client-visible consequence. Pay-rate gaps to local competitors predict attrition better than any engagement program. Read with first-90-day attrition and contract churn in accounts hit by staffing gaps.

## Formula

```
Guards Leaving / Guards Employed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** security_services_guarding
- **Sector:** security

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2056 (batch 6)
