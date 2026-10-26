# dea:metric-security-control-coverage

Candidate Performance Metric record for **Security Control Coverage** (SCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-control-coverage`
- **Name:** Security Control Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SCC

## 2. Definition

Security Control Coverage (SCC) measures conformance to standards, plans, or obligations in the Cybersecurity domain. The formula is Implemented Controls / Required Controls per Framework - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The share of systems, environments, or in-scope assets on which required security controls are actually deployed and enforced - the compliance-flavored metric that measures whether the security architecture exists in reality rather than in policy. Its strategic weight is the exposure arithmetic: an organization with 95 percent coverage has 1 in 20 systems unprotected, and attackers do not average - they find the uncovered tail, which is why coverage metrics are read at the tail, not the mean. Control frameworks (CIS, NIST, ISO 27001) supply the control definitions, and coverage against a framework is what certification actually measures. The gaming risk is scope definition - environments excluded from the denominator flatter the percentage - so the honest report publishes the denominator with the coverage number.

## Formula

```
Implemented Controls / Required Controls per Framework
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cybersecurity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 327 (batch 1)
