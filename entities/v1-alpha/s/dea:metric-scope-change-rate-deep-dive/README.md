# dea:metric-scope-change-rate-deep-dive

Candidate Performance Metric record for **Scope Change Rate (Deep Dive)** (SCR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-scope-change-rate-deep-dive`
- **Name:** Scope Change Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCR-D

## 2. Definition

Within Project Management (Deep Dive), Scope Change Rate (Deep Dive) (SCR-D) is used to gauge exposure to adverse outcomes. Its calculation is Approved Changes / Baseline Scope Items, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures the frequency and size of approved changes against the original scope. Scope change is a major source of both variance and stakeholder mistrust. A near-zero rate on exploratory projects may signal suppressed bad news rather than stability. Read with baseline change approval compliance and requirements volatility.

## Formula

```
SCR-D = Approved Changes / Baseline Scope Items
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2936 (batch 7)
