# dea:metric-base-station-downtime-per-quarter

Candidate Performance Metric record for **Base Station Downtime per Quarter** (BSDT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-base-station-downtime-per-quarter`
- **Name:** Base Station Downtime per Quarter
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BSDT

## 2. Definition

A Telecom Network Operations indicator, Base Station Downtime per Quarter (BSDT) quantifies the quality of outputs and outcomes. The formula is Total Site Unavailability Hours per Quarter - reported in hours. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Telecommunications sector.

## Formula

```
BSDT = Total Site Unavailability Hours per Quarter
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 861 (batch 3)
