# dea:metric-phase-transition-success-rate

Candidate Performance Metric record for **Phase Transition Success Rate** (PTSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-phase-transition-success-rate`
- **Name:** Phase Transition Success Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PTSR

## 2. Definition

A Pharma R&D & Clinical Trials indicator, Phase Transition Success Rate (PTSR) quantifies how effectively a process or entity achieves its intended outcome. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Compounds Advancing to Next Phase / Compounds in Phase - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Pharmaceuticals sector.

## 3. Context

Measures the share of candidates advancing across each clinical phase boundary. Phase II to III is the industry's most consequential filter, where biology either validates the mechanism or not. Portfolio-level probabilities of success anchor R&D economics and valuation, so definitional consistency (what counts as advancement) is everything. Read with pipeline attrition rate and R&D pipeline value composition.

## Formula

```
PTSR = Compounds Advancing to Next Phase / Compounds in Phase
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** pharma_r_d_clinical_trials
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1614 (batch 6)
