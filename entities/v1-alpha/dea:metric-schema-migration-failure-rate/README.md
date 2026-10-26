# dea:metric-schema-migration-failure-rate

Candidate Performance Metric record for **Schema Migration Failure Rate** (SMFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-schema-migration-failure-rate`
- **Name:** Schema Migration Failure Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SMFR

## 2. Definition

Schema Migration Failure Rate (SMFR) addresses the quality of outputs and outcomes and is a fixture of database & data platform operations reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Failed Migrations / Migration Attempts - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Software sector.

## Formula

```
SMFR = Failed Migrations / Migration Attempts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** database_data_platform_operations
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3231 (batch 7)
