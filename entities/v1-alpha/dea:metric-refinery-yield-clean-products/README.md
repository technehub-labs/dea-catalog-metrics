# dea:metric-refinery-yield-clean-products

Candidate Performance Metric record for **Refinery Yield - Clean Products** (RYCP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-refinery-yield-clean-products`
- **Name:** Refinery Yield - Clean Products
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RYCP

## 2. Definition

A Oil & Gas Downstream & Refining indicator, Refinery Yield - Clean Products (RYCP) quantifies how efficiently resources are converted into outputs. Its calculation is Clean Product Barrels / Crude Barrels, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Oil & Gas practice.

## 3. Context

Measures the share of crude converted into high-value light products (gasoline, diesel, jet) versus bottoms. It is the margin-engine metric of refining: product slate determines realized crack spreads, and yield improvements through configuration upgrades are worth more than most operational programs. Yield traded against severity energy cost is the real optimization. Read with energy intensity index - Refining and market capture ratio (Refining).

## Formula

```
Clean Product Barrels / Crude Barrels
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** oil_gas_downstream_refining
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2299 (batch 6)
