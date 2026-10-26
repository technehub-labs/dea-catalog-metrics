# dea:metric-jitter

Candidate Performance Metric record for **Jitter** (JTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-jitter`
- **Name:** Jitter
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** JTR

## 2. Definition

Within Telecom Network Operations, Jitter (JTR) is used to gauge the quality of outputs and outcomes. It is a working-level control: thresholds trigger immediate operational response. It is defined as Mean Variation in Packet Arrival Delay; the result is stated in seconds. It should be driven down, since lower readings signal healthier performance. In Telecommunications, it is a recognized element of the standard performance toolkit.

## Formula

```
Mean Variation in Packet Arrival Delay
```

## Unit

- **Unit reference:** `dea:unit-seconds`
- **Unit:** seconds
- **Unit label (as published):** seconds

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 866 (batch 3)
