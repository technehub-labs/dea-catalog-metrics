# dea:metric-strategic-headcount-gap-ratio

Candidate Performance Metric record for **Strategic Headcount Gap Ratio** (SHGR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-strategic-headcount-gap-ratio`
- **Name:** Strategic Headcount Gap Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SHGR

## 2. Definition

Strategic Headcount Gap Ratio (SHGR) addresses exposure to adverse outcomes and is a fixture of workforce planning & productivity reporting. It is defined as Critical Capability Roles Unfilled / Critical Capability Roles; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the gap between the workforce the strategy requires and the one in place. Strategic gaps are the human-capital form of execution risk. Gap definitions dominated by current org structure miss emerging roles. Read with critical skill coverage ratio and workforce plan accuracy.

## Formula

```
SHGR = Critical Capability Roles Unfilled / Critical Capability Roles
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_productivity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3896 (batch 8)
