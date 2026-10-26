# dea:metric-legacy-interface-dependency-ratio

Candidate Performance Metric record for **Legacy Interface Dependency Ratio** (LIDR-SA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-legacy-interface-dependency-ratio`
- **Name:** Legacy Interface Dependency Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LIDR-SA

## 2. Definition

Legacy Interface Dependency Ratio (LIDR-SA) measures exposure to adverse outcomes in the Software Architecture & Technical Design domain. It is defined as Calls to Legacy Systems / Total External Calls; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of system interactions routed through legacy interfaces (mainframe connectors, batch files, point-to-point links). Legacy interfaces are the impedance mismatch of modernization: they throttle data latency, constrain API-era integration, and concentrate fragile knowledge in aging middleware, and the ratio tracks the exit path. Ratio reduction must distinguish decommissioned interfaces from wrapped ones, since wrapping modernizes the appearance, not the coupling. Read with legacy system migration progress and integration incident rates.

## Formula

```
Calls to Legacy Systems / Total External Calls
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_architecture_technical_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2629 (batch 7)
