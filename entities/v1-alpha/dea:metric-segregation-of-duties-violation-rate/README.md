# dea:metric-segregation-of-duties-violation-rate

Candidate Performance Metric record for **Segregation of Duties Violation Rate** (SODVR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-segregation-of-duties-violation-rate`
- **Name:** Segregation of Duties Violation Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SODVR

## 2. Definition

Within Identity & Access Management Operations, Segregation of Duties Violation Rate (SODVR) is used to gauge exposure to adverse outcomes. It is defined as SoD Conflicts Detected per Period; the result is stated in count (items per period). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the frequency of users holding conflicting duty combinations (e.g., creating and approving payments). SoD failures convert individual error or malice into uncontrolled fraud. Violations tolerated as documented exceptions normalize the risk. Read with access recertification completion rate and privileged account ratio.

## Formula

```
SoD Conflicts Detected per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** identity_access_management_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2827 (batch 7)
