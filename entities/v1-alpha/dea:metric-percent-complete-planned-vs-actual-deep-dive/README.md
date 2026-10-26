# dea:metric-percent-complete-planned-vs-actual-deep-dive

Candidate Performance Metric record for **Percent Complete Planned vs Actual (Deep Dive)** (PCPA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-percent-complete-planned-vs-actual-deep-dive`
- **Name:** Percent Complete Planned vs Actual (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PCPA-D

## 2. Definition

Percent Complete Planned vs Actual (Deep Dive) (PCPA-D) captures conformance to standards, plans, or obligations for organizations tracking construction contracting (deep dive). It is computed as Actual Percent Complete - Planned Percent Complete, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is concentrated in Construction.

## 3. Context

Measures earned progress against planned progress on construction projects. It is the project-control fundamental: schedule slippage compounds in construction (trade stacking, weather windows, liquidated damages), and early variance detection is the only affordable correction point. Percent-complete estimation is the honesty battleground - subjective progress claims routinely diverge from physical completion, so validate against earned-value or milestone evidence. Read with site rework cost ratio (Deep Dive) and cash-flow draw versus progress.

## Formula

```
Actual Percent Complete - Planned Percent Complete
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** construction_contracting_deep_dive
- **Sector:** construction

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2396 (batch 6)
