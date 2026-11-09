# dea:metric-multi-tenancy-isolation-compliance

Candidate Performance Metric record for **Multi-Tenancy Isolation Compliance** (MTIC-SA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-multi-tenancy-isolation-compliance`
- **Name:** Multi-Tenancy Isolation Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MTIC-SA

## 2. Definition

A Software Architecture & Technical Design indicator, Multi-Tenancy Isolation Compliance (MTIC-SA) quantifies exposure to adverse outcomes. Its calculation is Isolation Tests Passed / Isolation Tests, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether tenant data, compute, and access boundaries meet isolation standards in multi-tenant platforms. Isolation failures are the catastrophic breach class of SaaS - one tenant's data reaching another is existential for the platform business - and compliance must be tested at the enforcement layer, not the design layer. Compliance must cover noisy-neighbor performance isolation as well as data isolation. Read with penetration-test findings on boundary controls and tenant data-access audit results.

## Formula

```
MTIC-SA = Isolation Tests Passed / Isolation Tests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_architecture_technical_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2638 (batch 7)
