# dea:metric-planned-to-reactive-maintenance-ratio-deep-dive

Candidate Performance Metric record for **Planned-to-Reactive Maintenance Ratio (Deep Dive)** (PRMR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-planned-to-reactive-maintenance-ratio-deep-dive`
- **Name:** Planned-to-Reactive Maintenance Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PRMR-D

## 2. Definition

Planned-to-Reactive Maintenance Ratio (Deep Dive) (PRMR-D) captures how efficiently resources are converted into outputs for organizations tracking facility management & workplace (deep dive). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Planned Maintenance Hours / Reactive Hours, measured in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of maintenance work that is planned versus reactive. It is the discipline metric of facilities operations: reactive work costs multiples of planned, degrades asset life, and concentrates into emergency budgets that crowd out preventive programs. Ratio improvement from deferring reactive work (backlog growth) is false discipline, so track backlog aging alongside. Read with asset condition indices and maintenance backlog value trends.

## Formula

```
Planned Maintenance Hours / Reactive Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2240 (batch 6)
