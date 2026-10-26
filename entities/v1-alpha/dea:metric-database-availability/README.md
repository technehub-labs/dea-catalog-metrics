# dea:metric-database-availability

Candidate Performance Metric record for **Database Availability** (DBAVL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-database-availability`
- **Name:** Database Availability
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DBAVL

## 2. Definition

Within Database & Data Platform Operations, Database Availability (DBAVL) is used to gauge the quality of outputs and outcomes. It is a working-level control: thresholds trigger immediate operational response. It is defined as Database Service Uptime in Period; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Software, it is a recognized element of the standard performance toolkit.

## Formula

```
DBAVL = Database Service Uptime in Period
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3228 (batch 7)
