# dea:metric-refinery-utilization-rate-deep-dive

Candidate Performance Metric record for **Refinery Utilization Rate (Deep Dive)** (RUR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-refinery-utilization-rate-deep-dive`
- **Name:** Refinery Utilization Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RUR

## 2. Definition

Refinery Utilization Rate (Deep Dive) (RUR) addresses the utilization or availability of capacity and is a fixture of oil & gas downstream & refining reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Barrels Processed per Day / Crude Distillation Capacity - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Oil & Gas sector.

## 3. Context

Measures crude throughput against rated capacity. It is the fixed-cost absorption metric of refining, a business with brutal economies of scale and thin crack-dependent margins, and utilization swings translate profit directly. Utilization above sustainable levels burns maintenance intervals, so read with turnaround integrity. Read with market capture ratio (Refining) and unplanned unit downtime (Refining).

## Formula

```
Barrels Processed per Day / Crude Distillation Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2297 (batch 6)
