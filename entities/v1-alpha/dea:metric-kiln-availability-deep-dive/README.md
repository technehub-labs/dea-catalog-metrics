# dea:metric-kiln-availability-deep-dive

Candidate Performance Metric record for **Kiln Availability (Deep Dive)** (KA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-kiln-availability-deep-dive`
- **Name:** Kiln Availability (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** KA-D

## 2. Definition

Kiln Availability (Deep Dive) (KA-D) measures the utilization or availability of capacity in the Cement & Building Materials domain. It is defined as Kiln Operating Hours / Planned Hours; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Manufacturing, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of time the kiln operates versus total time. Kilns are the capacity-constraining asset in cement, and unplanned downtime is brutally expensive because restarts are slow and refractory damage compounds. Availability improvements are worth more than most cost programs, but availability raised by deferring refractory maintenance is borrowed. Read with refractory campaign life and unplanned stop root causes.

## Formula

```
Kiln Operating Hours / Planned Hours
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cement_building_materials
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1865 (batch 6)
