# dea:metric-renewable-power-purchase-coverage

Candidate Performance Metric record for **Renewable Power Purchase Coverage** (RPPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-renewable-power-purchase-coverage`
- **Name:** Renewable Power Purchase Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RPPC

## 2. Definition

A Operations Energy Management indicator, Renewable Power Purchase Coverage (RPPC) quantifies environmental and social sustainability performance. The formula is Consumption under Renewable Contracts / Total Consumption - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of electricity consumption covered by renewable power purchase agreements or on-site generation, typically against a total consumption baseline. It is the primary instrument for scope 2 decarbonization commitments and increasingly a customer and investor expectation. Read the fine print: annual matching versus hourly matching, certificate unbundling, and additionality claims differ enormously in impact. Read with emissions intensity and hedging cost of the PPA portfolio.

## Formula

```
RPPC = Consumption under Renewable Contracts / Total Consumption
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** operations_energy_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1435 (batch 5)
