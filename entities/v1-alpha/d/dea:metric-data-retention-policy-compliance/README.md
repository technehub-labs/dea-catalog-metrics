# dea:metric-data-retention-policy-compliance

Candidate Performance Metric record for **Data Retention Policy Compliance** (DRPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-retention-policy-compliance`
- **Name:** Data Retention Policy Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DRPC

## 2. Definition

Within Database & Data Platform Operations, Data Retention Policy Compliance (DRPC) is used to gauge conformance to standards, plans, or obligations. Its calculation is Stores Compliant with Retention Schedule / Stores, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Software practice.

## Formula

```
DRPC = Stores Compliant with Retention Schedule / Stores
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** database_data_platform_operations
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3241 (batch 7)
