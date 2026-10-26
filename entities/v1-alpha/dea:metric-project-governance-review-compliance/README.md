# dea:metric-project-governance-review-compliance

Candidate Performance Metric record for **Project Governance Review Compliance** (PGRC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-project-governance-review-compliance`
- **Name:** Project Governance Review Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PGRC

## 2. Definition

Project Governance Review Compliance (PGRC) measures conformance to standards, plans, or obligations in the Project Management (Deep Dive) domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Gate Reviews Completed per Plan / Planned; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of projects conducting required stage and governance reviews. Governance reviews are the mechanism that catches troubled projects early. Compliance as scheduling theater without honest status reporting changes nothing. Read with stage gate bypass rate and project portfolio health distribution.

## Formula

```
PGRC = Gate Reviews Completed per Plan / Planned
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2938 (batch 7)
