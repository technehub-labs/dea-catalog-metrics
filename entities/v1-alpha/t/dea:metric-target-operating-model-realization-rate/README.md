# dea:metric-target-operating-model-realization-rate

Candidate Performance Metric record for **Target Operating Model Realization Rate** (TOMRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-target-operating-model-realization-rate`
- **Name:** Target Operating Model Realization Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TOMRR

## 2. Definition

Target Operating Model Realization Rate (TOMRR) addresses how effectively a process or entity achieves its intended outcome and is a fixture of operating model monitoring & design effectiveness reporting. The formula is Implemented TOM Components / Designed Components - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures progress against the designed target operating model. TOM programs are multi-year and drift without a realization scoreboard. Realization scored by workstream completion rather than outcome adoption overstates progress. Read with operating model change adoption rate and value stream cycle time.

## Formula

```
TOMRR = Implemented TOM Components / Designed Components
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** effectiveness
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** operating_model_monitoring_design_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3114 (batch 7)
