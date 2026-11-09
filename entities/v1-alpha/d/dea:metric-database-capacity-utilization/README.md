# dea:metric-database-capacity-utilization

Candidate Performance Metric record for **Database Capacity Utilization** (DBCU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-database-capacity-utilization`
- **Name:** Database Capacity Utilization
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DBCU

## 2. Definition

Database Capacity Utilization (DBCU) measures the utilization or availability of capacity in the Database & Data Platform Operations domain. Its calculation is Used Storage / Provisioned Storage, measured in percent (%). It provides the day-to-day signal that a process is running as designed. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. It originates from and is most used in Software practice.

## Formula

```
DBCU = Used Storage / Provisioned Storage
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** database_data_platform_operations
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3233 (batch 7)
