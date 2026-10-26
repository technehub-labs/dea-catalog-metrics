# dea:metric-legacy-system-migration-progress

Candidate Performance Metric record for **Legacy System Migration Progress** (LSMP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-legacy-system-migration-progress`
- **Name:** Legacy System Migration Progress
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LSMP

## 2. Definition

Legacy System Migration Progress (LSMP) addresses transformation and is a fixture of digital transformation reporting. Its calculation is Workloads or Functions Migrated / Functions in Scope, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures completion of planned migrations off legacy platforms, expressed in workloads, data volumes, or decommissioned applications. It is the pacing metric for whether transformation ends in a modern stack or a museum with a new gift shop. The honest read tracks decommissioning, not deployment: parallel-running both old and new is invisible cost, and migration pauses that linger for quarters rarely resume. Read with legacy cost run-rate reduction and application portfolio rationalization.

## Formula

```
Workloads or Functions Migrated / Functions in Scope
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** transformation
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** digital_transformation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1312 (batch 5)
