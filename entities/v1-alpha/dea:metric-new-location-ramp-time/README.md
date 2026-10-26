# dea:metric-new-location-ramp-time

Candidate Performance Metric record for **New Location Ramp Time** (NLRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-new-location-ramp-time`
- **Name:** New Location Ramp Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NLRT

## 2. Definition

New Location Ramp Time (NLRT) measures how efficiently resources are converted into outputs in the Franchise & Multi-site domain. It is defined as Months from Opening to Break-even Sales; the result is stated in days. In Franchise & multi-site, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

New location ramp time measures how long a new unit takes to reach mature revenue or profitability benchmarks, and it is the pacing metric for expansion capital - the faster units mature, the shorter the cash cycle that funds further growth, which is why ramp time sits at the center of franchise growth models. Ramp varies systematically by format maturity (new concepts ramp slower than proven ones), site quality, and market density, so blended averages mislead. The gaming risk is benchmark selection: setting the mature threshold low makes ramps look fast while masking underperformance. Read with the ramp curve shape (fast-then-plateau versus steady-climb), first-year unit loss rate, and cannibalization of adjacent units.

## Formula

```
Months from Opening to Break-even Sales
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** franchise_multi_site
- **Sector:** franchise_multi_site

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 806 (batch 2)
