# dea:metric-cargo-damage-claim-rate-maritime

Candidate Performance Metric record for **Cargo Damage Claim Rate (Maritime)** (CDRM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cargo-damage-claim-rate-maritime`
- **Name:** Cargo Damage Claim Rate (Maritime)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CDRM

## 2. Definition

A Maritime & Shipping indicator, Cargo Damage Claim Rate (Maritime) (CDRM) quantifies exposure to adverse outcomes. It is defined as Claims Value / Freight Revenue; the result is stated in percent (%). In Maritime & shipping, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures damage claims relative to cargo volume or value carried. It matters because cargo integrity is the core promise of shipping lines and terminal operators. Claims can be suppressed by onerous documentation requirements that deter legitimate filing. Read with Cargo Handover Inspection findings and insurance premium trends to confirm damage reduction is real.

## Formula

```
Claims Value / Freight Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping
- **Sector:** maritime_shipping

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 983 (batch 3)
