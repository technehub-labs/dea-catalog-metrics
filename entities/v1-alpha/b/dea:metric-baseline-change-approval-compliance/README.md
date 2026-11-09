# dea:metric-baseline-change-approval-compliance

Candidate Performance Metric record for **Baseline Change Approval Compliance** (BCAC-PM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-baseline-change-approval-compliance`
- **Name:** Baseline Change Approval Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BCAC-PM

## 2. Definition

Baseline Change Approval Compliance (BCAC-PM) addresses conformance to standards, plans, or obligations and is a fixture of project management (deep dive) reporting. The formula is Baseline Changes with Approved Change Request / Changes - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of baseline changes (scope, schedule, budget) processed through formal change control. Informal baseline drift makes all variance metrics meaningless. Compliance that approves virtually everything is a tollbooth, not control. Read with scope change rate and stage gate bypass rate.

## Formula

```
BCAC-PM = Baseline Changes with Approved Change Request / Changes
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2956 (batch 7)
