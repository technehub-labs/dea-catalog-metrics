# dea:metric-mine-plan-adherence

Candidate Performance Metric record for **Mine Plan Adherence** (MPA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mine-plan-adherence`
- **Name:** Mine Plan Adherence
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MPA

## 2. Definition

A Mining & Metals indicator, Mine Plan Adherence (MPA) quantifies conformance to standards, plans, or obligations. The formula is Actual Extraction vs Plan Tonnage and Grade / Plan - reported in percent (%). It is a standard measure in the Mining & metals sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures actual versus planned production, sequencing, and grade delivery in mining. It matters because mills and sales contracts are tuned to planned grade and tonnage. Chasing adherence can push mining into lower-grade zones to hit tonnage, hurting realized grade. Read with Ore Grade trends and Cost per Tonne to confirm adherence is balanced, not tonnage-biased.

## Formula

```
MPA = Actual Extraction vs Plan Tonnage and Grade / Plan
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** mining_metals
- **Sector:** mining_metals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 724 (batch 2)
