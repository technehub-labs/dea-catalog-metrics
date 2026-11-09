# dea:metric-radio-access-network-utilization

Candidate Performance Metric record for **Radio Access Network Utilization** (RANU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-radio-access-network-utilization`
- **Name:** Radio Access Network Utilization
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RANU

## 2. Definition

Within Telecom Network Operations, Radio Access Network Utilization (RANU) is used to gauge the utilization or availability of capacity. Its calculation is Used Radio Capacity / Provisioned Radio Capacity, measured in percent (%). It originates from and is most used in Telecommunications practice. Its value drives prioritization and resource reallocation among competing initiatives. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures capacity utilization of radio network elements. It matters because utilization balance determines both capital efficiency and customer-experienced quality. Sustained peaks above 70-80 percent drive congestion that degrades user experience before the metric shows crisis. Read with Network Latency and Throughput metrics to confirm utilization is not silently degrading experience.

## Formula

```
RANU = Used Radio Capacity / Provisioned Radio Capacity
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 863 (batch 3)
