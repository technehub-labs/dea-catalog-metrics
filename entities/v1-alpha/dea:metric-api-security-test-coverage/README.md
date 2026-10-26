# dea:metric-api-security-test-coverage

Candidate Performance Metric record for **API Security Test Coverage** (APSTC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-security-test-coverage`
- **Name:** API Security Test Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** APSTC

## 2. Definition

API Security Test Coverage (APSTC) captures exposure to adverse outcomes for organizations tracking devsecops & application security engineering. It is defined as APIs with Security Test Suite / Exposed APIs; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of APIs with automated security tests covering authentication, authorization, and injection classes. APIs now carry most of the attack surface and are a top breach vector, often exposed via undocumented endpoints. Coverage of documented endpoints misses shadow APIs entirely. Read with DAST coverage of attack surface and OWASP Top 10 regression coverage.

## Formula

```
APIs with Security Test Suite / Exposed APIs
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2762 (batch 7)
