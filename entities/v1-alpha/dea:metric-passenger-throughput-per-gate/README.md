# dea:metric-passenger-throughput-per-gate

Candidate Performance Metric record for **Passenger Throughput per Gate** (PTPG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-passenger-throughput-per-gate`
- **Name:** Passenger Throughput per Gate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PTPG

## 2. Definition

Passenger Throughput per Gate (PTPG) measures the utilization or availability of capacity in the Airport Operations domain. It is computed as Passengers Processed / Gates per Period, expressed in ratio (x:1 or x). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Airports.

## 3. Context

Measures passengers processed per gate per period. It matters because gate productivity caps airport capacity without capital expansion. Pushing throughput past design loads degrades passenger experience and turnaround reliability. Read with On-Time Performance at gates and Passenger Satisfaction to confirm throughput coexists with service quality.

## Formula

```
Passengers Processed / Gates per Period
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations
- **Sector:** airports

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1176 (batch 4)
