# dea:metric-vessel-on-time-arrival-rate-deep-dive

Candidate Performance Metric record for **Vessel On-Time Arrival Rate (Deep Dive)** (VOTA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vessel-on-time-arrival-rate-deep-dive`
- **Name:** Vessel On-Time Arrival Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** VOTA-D

## 2. Definition

Vessel On-Time Arrival Rate (Deep Dive) (VOTA-D) measures conformance to standards, plans, or obligations in the Maritime Shipping (Deep Dive) domain. The formula is Arrivals within Window / Port Calls - reported in percent (%). It is a standard measure in the Maritime sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures schedule reliability of vessel arrivals within tolerance windows. Ocean schedule reliability collapsed in recent disruption years, and it is the anchor metric of supply-chain planning for every shipper: contract design, safety stock, and mode mix all price off arrival reliability. Relaxing the arrival tolerance window is the standard gaming move, so window definitions belong in the read. Read with port congestion indices and downstream supply chain service levels.

## Formula

```
VOTA-D = Arrivals within Window / Port Calls
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping_deep_dive
- **Sector:** maritime

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2430 (batch 6)
