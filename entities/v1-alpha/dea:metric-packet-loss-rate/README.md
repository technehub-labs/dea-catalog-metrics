# dea:metric-packet-loss-rate

Candidate Performance Metric record for **Packet Loss Rate** (PLR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-packet-loss-rate`
- **Name:** Packet Loss Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PLR

## 2. Definition

A Telecom Network Operations indicator, Packet Loss Rate (PLR) quantifies the quality of outputs and outcomes. Its calculation is Lost Packets / Packets Transmitted, measured in percent (%). It originates from and is most used in Telecommunications practice. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Lost Packets / Packets Transmitted
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 865 (batch 3)
