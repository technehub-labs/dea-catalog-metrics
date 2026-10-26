# dea:metric-standard-parts-utilization

Candidate Performance Metric record for **Standard Parts Utilization** (SPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-standard-parts-utilization`
- **Name:** Standard Parts Utilization
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SPU

## 2. Definition

Standard Parts Utilization (SPU) measures how efficiently resources are converted into outputs in the Engineering & Design domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Standard or Catalog Parts / Total Parts - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of bills of material composed of standard, preferred, or catalog parts rather than bespoke designs. Standards adoption is the unglamorous lever on cost, supply resilience, and quality, since every unique part multiplies SKU complexity and qualification effort. Watch for nominal standards lists that engineers route around, and count utilization after design release, not at concept. Read with design reuse rate and supplier rationalization trends.

## Formula

```
Standard or Catalog Parts / Total Parts
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** engineering_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1772 (batch 6)
