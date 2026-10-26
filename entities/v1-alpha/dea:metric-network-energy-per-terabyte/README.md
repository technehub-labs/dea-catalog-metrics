# dea:metric-network-energy-per-terabyte

Candidate Performance Metric record for **Network Energy per Terabyte** (NET-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-network-energy-per-terabyte`
- **Name:** Network Energy per Terabyte
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NET-T

## 2. Definition

Within Telecom Network Operations (Deep Dive), Network Energy per Terabyte (NET-T) is used to gauge environmental and social sustainability performance. Its calculation is Energy Consumed / Data Carried, measured in megawatt-hours (MWh). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. It originates from and is most used in Telecommunications practice.

## 3. Context

Measures network energy consumption per unit of data carried. Energy is the largest controllable opex line of network operations, traffic growth compounds it, and efficiency per terabyte is the metric that separates disciplined operators from those deploying capacity faster than they can power it. Read by network layer (RAN dominates) and traffic mix. Read with site energy-efficiency programs and renewable power purchase coverage for emissions.

## Formula

```
Energy Consumed / Data Carried
```

## Unit

- **Unit reference:** `dea:unit-megawatthours`
- **Unit:** megawatthours
- **Unit label (as published):** megawatt-hours (MWh)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations_deep_dive
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2137 (batch 6)
