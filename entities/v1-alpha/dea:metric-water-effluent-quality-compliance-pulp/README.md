# dea:metric-water-effluent-quality-compliance-pulp

Candidate Performance Metric record for **Water Effluent Quality Compliance (Pulp)** (WEQC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-water-effluent-quality-compliance-pulp`
- **Name:** Water Effluent Quality Compliance (Pulp)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** WEQC

## 2. Definition

Water Effluent Quality Compliance (Pulp) (WEQC) measures conformance to standards, plans, or obligations in the Pulp, Paper & Forest Products domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Discharges within Permit / Discharges Tested, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Manufacturing.

## 3. Context

Measures treated mill effluent against permitted parameters - BOD, COD, AOX, temperature. Pulp mills live or die by effluent performance in their watersheds, and exceedances carry both enforcement and community legitimacy costs. Read parameter-specific trends rather than pass-fail, since chronic near-limit operation precedes violations. Read with treatment system availability and spill event reporting.

## Formula

```
Discharges within Permit / Discharges Tested
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pulp_paper_forest_products
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1861 (batch 6)
