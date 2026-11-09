# dea:metric-master-data-sync-latency

Candidate Performance Metric record for **Master Data Sync Latency** (MDSL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-master-data-sync-latency`
- **Name:** Master Data Sync Latency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MDSL

## 2. Definition

Master Data Sync Latency (MDSL) captures the quality of outputs and outcomes for organizations tracking master data management. It provides the day-to-day signal that a process is running as designed. Its calculation is Propagation Delay from Master Update to Subscribing Systems, measured in minutes. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
MDSL = Propagation Delay from Master Update to Subscribing Systems
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** master_data_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3640 (batch 8)
