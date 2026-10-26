# dea:metric-milestone-adherence

Candidate Performance Metric record for **Milestone Adherence** (MA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-milestone-adherence`
- **Name:** Milestone Adherence
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MA

## 2. Definition

Milestone Adherence (MA) measures conformance to standards, plans, or obligations in the Project Management domain. Its calculation is Milestones Met on Time / Milestones Planned, measured in percent (%). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of project milestones completed on schedule. It matters because milestone slips are the earliest objective signal of scope or plan trouble. Teams can hold the metric green by re-baselining milestones rather than fixing slippage causes. Read with Schedule Performance Index and Baseline Scope Stability to detect re-baselining masking real delay.

## Formula

```
Milestones Met on Time / Milestones Planned
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 353 (batch 1)
