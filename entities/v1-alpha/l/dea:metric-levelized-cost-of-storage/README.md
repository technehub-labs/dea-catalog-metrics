# dea:metric-levelized-cost-of-storage

Candidate Performance Metric record for **Levelized Cost of Storage** (LCOS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-levelized-cost-of-storage`
- **Name:** Levelized Cost of Storage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LCOS

## 2. Definition

Levelized Cost of Storage (LCOS) captures the economic value created or preserved for organizations tracking energy transition & renewables. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Lifetime Storage Costs / Energy Delivered from Storage, measured in currency per unit. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Renewable energy practice.

## 3. Context

Levelized cost of storage (LCOS) is the discounted lifetime cost per unit of energy discharged - the storage-equivalent of LCOE for batteries and other storage technologies - and it is the metric that prices the flexibility gap between renewable generation and demand timing. The construction is complex because storage's cost depends on cycling pattern: a battery cycled daily (solar shifting) amortizes capital over far more cycles than one used for occasional peak shaving or resilience, so the same physical asset has a completely different LCOS depending on its duty cycle. Revenue-stacking honesty matters as much as cost: storage earns from energy arbitrage, capacity markets, and frequency regulation simultaneously in advanced markets, so cost-per-use without revenue-per-use is half the picture. Read with cycle-life utilization, round-trip efficiency losses (LCOS includes them), and revenue-stack composition which determines whether the cost is recoverable.

## Formula

```
LCOS = Lifetime Storage Costs / Energy Delivered from Storage
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_transition_renewables
- **Sector:** renewable_energy

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1106 (batch 4)
