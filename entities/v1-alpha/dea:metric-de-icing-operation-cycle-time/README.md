# dea:metric-de-icing-operation-cycle-time

Candidate Performance Metric record for **De-Icing Operation Cycle Time** (DIO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-de-icing-operation-cycle-time`
- **Name:** De-Icing Operation Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DIO

## 2. Definition

A Airport Operations indicator, De-Icing Operation Cycle Time (DIO) quantifies how efficiently resources are converted into outputs. It is a working-level control: thresholds trigger immediate operational response. It is defined as Minutes to De-Ice Aircraft; the result is stated in minutes. It should be driven down, since lower readings signal healthier performance. In Airports, it is a recognized element of the standard performance toolkit.

## Formula

```
DIO = Minutes to De-Ice Aircraft
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations
- **Sector:** airports

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1183 (batch 4)
