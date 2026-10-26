# dea:metric-undocumented-api-discovery-rate

Candidate Performance Metric record for **Undocumented API Discovery Rate** (UADR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-undocumented-api-discovery-rate`
- **Name:** Undocumented API Discovery Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** UADR

## 2. Definition

A API Lifecycle Management indicator, Undocumented API Discovery Rate (UADR) quantifies exposure to adverse outcomes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Shadow Endpoints Discovered per Discovery Cycle - reported in count (items per period). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Software sector.

## Formula

```
Shadow Endpoints Discovered per Discovery Cycle
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** api_lifecycle_management
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3217 (batch 7)
