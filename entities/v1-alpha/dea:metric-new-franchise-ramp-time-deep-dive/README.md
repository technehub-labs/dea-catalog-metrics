# dea:metric-new-franchise-ramp-time-deep-dive

Candidate Performance Metric record for **New Franchise Ramp Time (Deep Dive)** (NFRM-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-new-franchise-ramp-time-deep-dive`
- **Name:** New Franchise Ramp Time (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NFRM-D

## 2. Definition

Within Franchise Operations (Deep Dive), New Franchise Ramp Time (Deep Dive) (NFRM-D) is used to gauge how efficiently resources are converted into outputs. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Months from Opening to Breakeven, measured in months. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures time from opening to defined viability milestones (breakeven, target volumes). It is the promise-keeping metric of franchising: candidates buy a system partly on ramp expectations, and slow ramps signal site selection, training, or market-fit failures. Ramp speed achieved through front-loaded promotional spend that fades after opening is borrowed time. Read with site-selection model accuracy and support intensity during the first year.

## Formula

```
Months from Opening to Breakeven
```

## Unit

- **Unit reference:** `dea:unit-month`
- **Unit:** month
- **Unit label (as published):** months

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** franchise_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2221 (batch 6)
