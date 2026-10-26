# dea:metric-unmonitored-critical-device-count

Candidate Performance Metric record for **Unmonitored Critical Device Count** (UCDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-unmonitored-critical-device-count`
- **Name:** Unmonitored Critical Device Count
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** UCDC

## 2. Definition

Within Network Operations Center (Deep Dive), Unmonitored Critical Device Count (UCDC) is used to gauge exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Critical Devices without Monitoring, expressed in count (items per period). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures critical network devices not covered by monitoring and alerting. Unmonitored devices fail silently, converting outages into discoveries. Counting depends entirely on the accuracy of the critical device inventory. Read with monitoring coverage ratio and NOC ticket resolution within SLA.

## Formula

```
Critical Devices without Monitoring
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** network_operations_center_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2843 (batch 7)
