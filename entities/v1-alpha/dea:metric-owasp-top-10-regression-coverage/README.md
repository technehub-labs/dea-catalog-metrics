# dea:metric-owasp-top-10-regression-coverage

Candidate Performance Metric record for **OWASP Top 10 Regression Coverage** (OT10RC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-owasp-top-10-regression-coverage`
- **Name:** OWASP Top 10 Regression Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OT10RC

## 2. Definition

OWASP Top 10 Regression Coverage (OT10RC) captures conformance to standards, plans, or obligations for organizations tracking devsecops & application security engineering. The formula is Top 10 Categories with Automated Regression Tests / Categories - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how well automated regression suites exercise the OWASP Top 10 vulnerability classes. These classes account for the overwhelming majority of application breaches. A suite can cover each category nominally without testing the authorization logic where real breaches happen. Read with API security test coverage and penetration test finding recurrence rate.

## Formula

```
Top 10 Categories with Automated Regression Tests / Categories
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** devsecops_application_security_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2763 (batch 7)
