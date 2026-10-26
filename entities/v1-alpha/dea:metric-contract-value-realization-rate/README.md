# dea:metric-contract-value-realization-rate

Candidate Performance Metric record for **Contract Value Realization Rate** (CVRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contract-value-realization-rate`
- **Name:** Contract Value Realization Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CVRR

## 2. Definition

Contract Value Realization Rate (CVRR) captures the economic value created or preserved for organizations tracking contract lifecycle management. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Realized Value vs Contracted Entitlements - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether negotiated contract value (discounts, service credits, rights) is actually claimed. Realization is where contract value is won or lost: unclaimed rights are donated money. Self-reported realization from the negotiating team grades its own homework. Read with value leakage from missed renewals and vendor management ROI.

## Formula

```
Realized Value vs Contracted Entitlements
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contract_lifecycle_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3711 (batch 8)
