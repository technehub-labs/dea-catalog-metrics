# dea:metric-smart-meter-installation-rate

Candidate Performance Metric record for **Smart Meter Installation Rate** (SMIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-smart-meter-installation-rate`
- **Name:** Smart Meter Installation Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SMIR

## 2. Definition

Smart Meter Installation Rate (SMIR) addresses capability maturity or development and is a fixture of utilities customer operations reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Smart Meters Installed / Meters in Service; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Utilities, it is a recognized element of the standard performance toolkit.

## 3. Context

Smart meter installation rate measures the share of premises with advanced metering infrastructure, and it is the foundational metric of grid modernization - nearly every downstream utility capability (time-of-use pricing, outage detection, demand response, dynamic load visibility) depends on meter coverage first. The rollout economics are distinctive: utilities deploy capital over a decade against regulatory approval with cost-recovery mechanisms, making installation rate a regulatory-program execution metric as much as a technology one. The last-mile problem is real: reaching 90 percent is programmatic, while the final holdouts (access issues, customer refusal, rental properties) require case-by-case effort with rising per-unit cost. Read with installation cost per meter trend, meter data collection success rate, opt-out rate, and downstream capability enablement (time-of-use enrollment, outage detection latency).

## Formula

```
Smart Meters Installed / Meters in Service
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** utilities_customer_operations
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 961 (batch 3)
