# dea:metric-server-utilization

Candidate Performance Metric record for **Server Utilization** (SVU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-server-utilization`
- **Name:** Server Utilization
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SVU

## 2. Definition

Server Utilization (SVU) measures the utilization or availability of capacity in the IT Service Management domain. Its calculation is Average CPU or Memory Utilization of Servers, measured in percent (%). It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. Values outside the intended band, on either side, warrant investigation.

## Formula

```
SVU = Average CPU or Memory Utilization of Servers
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 315 (batch 1)
