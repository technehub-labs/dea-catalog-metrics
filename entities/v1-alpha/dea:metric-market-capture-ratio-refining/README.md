# dea:metric-market-capture-ratio-refining

Candidate Performance Metric record for **Market Capture Ratio (Refining)** (MCR-R) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-market-capture-ratio-refining`
- **Name:** Market Capture Ratio (Refining)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MCR-R

## 2. Definition

A Oil & Gas Downstream & Refining indicator, Market Capture Ratio (Refining) (MCR-R) quantifies the economic value created or preserved. It is computed as Realized Crack Spread / Market Crack Spread, expressed in percent (%). Its use is concentrated in Oil & Gas. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Compares actual crack margins captured against benchmark market cracks. It is the commercial excellence metric of refining: it reveals how much of available market margin the refinery's configuration, scheduling, and trading capability actually monetize, and under-capture signals the fix is commercial, not operational. Benchmark selection is the honest-read battleground. Read with refinery yield - clean products and terminal netback analysis.

## Formula

```
MCR-R = Realized Crack Spread / Market Crack Spread
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2307 (batch 6)
