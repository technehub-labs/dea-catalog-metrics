# dea:metric-sales-per-square-meter

Candidate Performance Metric record for **Sales per Square Meter** (SPSM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sales-per-square-meter`
- **Name:** Sales per Square Meter
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SPSM

## 2. Definition

A Retail & E-commerce indicator, Sales per Square Meter (SPSM) quantifies how efficiently resources are converted into outputs. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Revenue / Sales Floor Area, measured in currency per unit. Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Retail practice.

## 3. Context

Revenue divided by selling area - the foundational productivity metric of physical retail, where real estate is the production capacity and this number is the output per unit of it. Its strategic significance is the productivity lens it forces: identical revenue in a larger box is worse retail, and the metric makes that visible store by store, which is why it anchors location strategy, format design, and the underperforming-store conversation. The honest comparison is like-for-like: flagship urban locations and suburban formats run at structurally different sales densities, so benchmarking uses format bands, and leased departments and non-selling area conventions can move the number materially. Read with gross margin per square meter - the refinement that resists high-density layouts filled with low-margin merchandise, which is how the unrefined metric is most commonly gamed.

## Formula

```
Revenue / Sales Floor Area
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_e_commerce
- **Sector:** retail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 486 (batch 1)
