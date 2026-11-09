# dea:metric-zero-downtime-migration-rate

Candidate Performance Metric record for **Zero-Downtime Migration Rate** (ZDTM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-zero-downtime-migration-rate`
- **Name:** Zero-Downtime Migration Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ZDTM

## 2. Definition

Zero-Downtime Migration Rate (ZDTM) addresses the quality of outputs and outcomes and is a fixture of database & data platform operations reporting. It is computed as Migrations with No Downtime / Migrations, expressed in percent (%). Its use is concentrated in Software. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
ZDTM = Migrations with No Downtime / Migrations
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** database_data_platform_operations
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3232 (batch 7)
