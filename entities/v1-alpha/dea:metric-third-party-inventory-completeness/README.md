# dea:metric-third-party-inventory-completeness

Candidate Performance Metric record for **Third-Party Inventory Completeness** (TPIC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-third-party-inventory-completeness`
- **Name:** Third-Party Inventory Completeness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TPIC

## 2. Definition

Third-Party Inventory Completeness (TPIC) captures exposure to adverse outcomes for organizations tracking third-party risk management. It is defined as Vendors Registered in TPRM System / Vendors Identified; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how completely the full vendor and supplier population is captured and classified. Uninventoried third parties are unassessed third parties. Inventories that exclude consultants, affiliates, and SaaS swipes miss whole risk classes. Read with third-party inventory completeness rate and shadow IT spend ratio.

## Formula

```
TPIC = Vendors Registered in TPRM System / Vendors Identified
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** third_party_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3715 (batch 8)
