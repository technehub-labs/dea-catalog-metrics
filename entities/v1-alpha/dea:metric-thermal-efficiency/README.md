# dea:metric-thermal-efficiency

Candidate Performance Metric record for **Thermal Efficiency** (THE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-thermal-efficiency`
- **Name:** Thermal Efficiency
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** THE

## 2. Definition

Thermal Efficiency (THE) measures how efficiently resources are converted into outputs in the Energy & Utilities domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Useful Energy Output / Fuel Energy Input, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Energy & utilities.

## 3. Context

The share of fuel energy converted to useful output - for a power plant, fuel input against electricity generated - the metric that determines fuel cost per unit of everything, since every percentage point of efficiency changes fuel spend by multiple percent. Its strategic significance is the efficiency-resource argument: improvements in heat rate historically delivered the cheapest marginal decarbonization available to the power sector, because less fuel per megawatt-hour is emissions reduction that pays for itself. Read against the reference-performance line (the design efficiency at rated conditions) rather than absolute levels: the gap between test-day performance and current performance is the recoverable degradation that maintenance and upgrades target, and honest trend analysis corrects for ambient temperature, load, and fuel quality before concluding the plant actually changed.

## Formula

```
Useful Energy Output / Fuel Energy Input
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_utilities
- **Sector:** energy_utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 440 (batch 1)
