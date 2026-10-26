# dea:metric-mean-time-to-repair-deep-dive

Candidate Performance Metric record for **Mean Time to Repair (Deep Dive)** (MTTR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-repair-deep-dive`
- **Name:** Mean Time to Repair (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MTTR-D

## 2. Definition

A Telecom Network Operations (Deep Dive) indicator, Mean Time to Repair (Deep Dive) (MTTR-D) quantifies how efficiently resources are converted into outputs. The formula is Hours from Fault to Restoration - reported in hours. It is a standard measure in the Telecommunications sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Hours from Fault to Restoration
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations_deep_dive
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2126 (batch 6)
