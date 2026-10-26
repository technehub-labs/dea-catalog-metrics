# dea:metric-concentration-risk-ratio

Candidate Performance Metric record for **Concentration Risk Ratio** (CRR-TP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-concentration-risk-ratio`
- **Name:** Concentration Risk Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CRR-TP

## 2. Definition

Within Third-Party Risk Management, Concentration Risk Ratio (CRR-TP) is used to gauge exposure to adverse outcomes. Its calculation is Spend with Top 10 Vendors / Total Vendor Spend, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures dependence on single vendors, geographies, or technologies across the third-party estate. Concentration converts vendor failure into portfolio failure. Ratios computed on spend rather than criticality underweight cheap-but-critical dependencies. Read with single-source dependency ratio and fourth-party visibility rate.

## Formula

```
Spend with Top 10 Vendors / Total Vendor Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** third_party_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3721 (batch 8)
