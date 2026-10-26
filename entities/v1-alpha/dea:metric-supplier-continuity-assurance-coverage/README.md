# dea:metric-supplier-continuity-assurance-coverage

Candidate Performance Metric record for **Supplier Continuity Assurance Coverage** (SCAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supplier-continuity-assurance-coverage`
- **Name:** Supplier Continuity Assurance Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SCAC

## 2. Definition

Supplier Continuity Assurance Coverage (SCAC) addresses exposure to adverse outcomes and is a fixture of business resilience & continuity reporting. The formula is Critical Suppliers with Continuity Assurance / Critical Suppliers - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of critical supplier spend or volume covered by continuity assurance - verified capacity commitments, dual sourcing, contingency contracts, exercised plans. Concentrated single-sourced supply is the most common resilience blind spot after IT. Assurance must be evidence-verified: untested supplier promises are coverage on paper only. Read with single point of failure count and supply disruption loss history.

## Formula

```
Critical Suppliers with Continuity Assurance / Critical Suppliers
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_resilience_continuity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1413 (batch 5)
