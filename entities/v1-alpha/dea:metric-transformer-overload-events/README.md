# dea:metric-transformer-overload-events

Candidate Performance Metric record for **Transformer Overload Events** (TOE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-transformer-overload-events`
- **Name:** Transformer Overload Events
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TOE

## 2. Definition

Within Utilities Field Operations & Grid, Transformer Overload Events (TOE) is used to gauge exposure to adverse outcomes. It is defined as Hours above Emergency Rating per Transformer; the result is stated in hours. In Utilities, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
TOE = Hours above Emergency Rating per Transformer
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** utilities_field_operations_grid
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1887 (batch 6)
