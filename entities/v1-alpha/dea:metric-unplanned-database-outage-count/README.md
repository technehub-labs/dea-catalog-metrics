# dea:metric-unplanned-database-outage-count

Candidate Performance Metric record for **Unplanned Database Outage Count** (UDO-CT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-unplanned-database-outage-count`
- **Name:** Unplanned Database Outage Count
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** UDO-CT

## 2. Definition

A Database & Data Platform Operations indicator, Unplanned Database Outage Count (UDO-CT) quantifies the quality of outputs and outcomes. It is defined as Unplanned Database Outages in Period; the result is stated in count (items per period). It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. In Software, it is a recognized element of the standard performance toolkit.

## Formula

```
UDO-CT = Unplanned Database Outages in Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3240 (batch 7)
