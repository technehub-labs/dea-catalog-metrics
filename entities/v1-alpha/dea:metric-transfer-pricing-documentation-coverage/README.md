# dea:metric-transfer-pricing-documentation-coverage

Candidate Performance Metric record for **Transfer Pricing Documentation Coverage** (TPDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-transfer-pricing-documentation-coverage`
- **Name:** Transfer Pricing Documentation Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TPDC

## 2. Definition

Transfer Pricing Documentation Coverage (TPDC) captures conformance to standards, plans, or obligations for organizations tracking tax & fiscal. Its calculation is Intercompany Flows with Documentation / Total Intercompany Flows, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of cross-border related-party transactions covered by compliant transfer-pricing documentation - the readiness metric of the intercompany pricing regime, whose strategic significance is audit exposure: tax authorities worldwide coordinate through information exchange, and undocumented flows are assessed by the authority's method, not the taxpayer's - with penalties added for the absence of documentation itself. The metric's weight rose with the global minimum-tax architecture and country-by-country reporting: intercompany pricing now sits under multiple overlapping lenses simultaneously, and coverage is the primary evidence of control when any of them focuses. The honest construction is materiality-tiered: covering the large flows with full functional analysis and the long tail with simplified support is the pragmatic standard, and coverage claimed without contemporaneous documentation (prepared before the audit, not during it) fails the test of the regimes that specifically reward it.

## Formula

```
Intercompany Flows with Documentation / Total Intercompany Flows
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
- **Domain:** tax_fiscal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 607 (batch 2)
