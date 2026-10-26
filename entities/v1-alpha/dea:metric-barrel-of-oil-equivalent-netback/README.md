# dea:metric-barrel-of-oil-equivalent-netback

Candidate Performance Metric record for **Barrel of Oil Equivalent Netback** (BOEN) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-barrel-of-oil-equivalent-netback`
- **Name:** Barrel of Oil Equivalent Netback
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BOEN

## 2. Definition

A Oil & Gas indicator, Barrel of Oil Equivalent Netback (BOEN) quantifies the economic value created or preserved. The formula is Revenue per Barrel - Lifting Cost - Transportation - Taxes - reported in currency value. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Oil & gas sector.

## 3. Context

The boe netback measures revenue per barrel equivalent minus royalties, operating costs, and transportation - the field-level cash margin that upstream companies disclose per-boe for comparability across their portfolios. It is the metric that reveals asset quality independent of scale, which is why investor presentations feature it so prominently. Its honest reading requires cost-boundary consistency: netbacks can be calculated before or after exploration expense, interest, and hedging, so cross-company comparisons fail without standardized definitions. Hedging distortion is especially important - realized prices versus benchmark prices diverge with hedge books in place. Read with netback by asset, cost structure decomposition (operating versus transportation versus royalty), and hedging gains or losses reconciling realized to benchmark pricing.

## Formula

```
Revenue per Barrel - Lifting Cost - Transportation - Taxes
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** oil_gas
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 892 (batch 3)
