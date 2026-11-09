# dea:metric-migration-currency-rate

Candidate Performance Metric record for **Migration Currency Rate** (MCRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-migration-currency-rate`
- **Name:** Migration Currency Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MCRR

## 2. Definition

A Records & Information Management indicator, Migration Currency Rate (MCRR) quantifies the quality of outputs and outcomes. Its calculation is Record Formats Migrated from Obsolete Formats / Obsolete Formats Identified, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether records are migrated to current storage formats and systems per schedule. Unmigrated records become unreadable: retention obligations persist while access dies. Migration measured by project plan rather than verified accessibility is nominal. Read with records disposition timeliness and legacy system decommissioning progress.

## Formula

```
MCRR = Record Formats Migrated from Obsolete Formats / Obsolete Formats Identified
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** records_information_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3685 (batch 8)
