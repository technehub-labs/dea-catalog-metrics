# dea:metric-space-utilization-rate-deep-dive

Candidate Performance Metric record for **Space Utilization Rate (Deep Dive)** (SUR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-space-utilization-rate-deep-dive`
- **Name:** Space Utilization Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SUR-D

## 2. Definition

Space Utilization Rate (Deep Dive) (SUR-D) addresses the utilization or availability of capacity and is a fixture of facility management & workplace (deep dive) reporting. Its calculation is Occupied or Booked Space / Total Space, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures actual use of workspace against available capacity. It is the economic case behind portfolio rationalization: office cost is fixed, and utilization data is what converts real estate from tradition into evidence-based decisions. Sensor-based measurement beats badge data (badges measure presence, not use), and hybrid patterns make time-sliced reads essential. Read with desk utilization rate (Deep Dive) and space cost per workstation.

## Formula

```
Occupied or Booked Space / Total Space
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facility_management_workplace_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2237 (batch 6)
