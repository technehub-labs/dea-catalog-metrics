# dea:metric-guard-licensing-compliance

Candidate Performance Metric record for **Guard Licensing Compliance** (GLC-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-guard-licensing-compliance`
- **Name:** Guard Licensing Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GLC-S

## 2. Definition

Guard Licensing Compliance (GLC-S) captures conformance to standards, plans, or obligations for organizations tracking security services & guarding. It is defined as Guards with Valid Licenses / Deployed Guards; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Security, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of security officers deployed with valid licenses and required training currency. An unlicensed guard on shift creates immediate legal exposure for the firm and its clients, and the risk concentrates in high-turnover bulk contracts. Real-time license-expiry tracking is the only reliable control, since annual audits sample a moving population. Read with guard attrition rate (Security) and contract-level deployment audits.

## Formula

```
Guards with Valid Licenses / Deployed Guards
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** security_services_guarding
- **Sector:** security

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2054 (batch 6)
