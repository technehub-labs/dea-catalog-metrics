# dea:metric-due-diligence-depth-compliance

Candidate Performance Metric record for **Due Diligence Depth Compliance** (DDDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-due-diligence-depth-compliance`
- **Name:** Due Diligence Depth Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DDDC

## 2. Definition

Due Diligence Depth Compliance (DDDC) captures conformance to standards, plans, or obligations for organizations tracking third-party risk management. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Vendors Receiving Tier-Appropriate Diligence / Vendors; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether initial due diligence met the required depth by risk tier. Diligence depth is what separates risk management from questionnaire collection. Standard questionnaires answered by vendors without evidence are compliance theater. Read with critical vendor assessment coverage and vendor risk incident rate.

## Formula

```
DDDC = Vendors Receiving Tier-Appropriate Diligence / Vendors
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3718 (batch 8)
