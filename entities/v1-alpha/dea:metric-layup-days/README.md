# dea:metric-layup-days

Candidate Performance Metric record for **Layup Days** (LUD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-layup-days`
- **Name:** Layup Days
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LUD

## 2. Definition

Layup Days (LUD) captures the utilization or availability of capacity for organizations tracking maritime & shipping. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Vessel Days Idle / Total Vessel Days; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. In Maritime & shipping, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures days vessels are laid up inactive rather than earning. It matters because laid-up tonnage is a direct read of overcapacity or uncompetitive positioning. Layups can be avoided by accepting uneconomic freight rates that move the loss from the balance sheet to the P&L. Read with Vessel Utilization and Freight Rate trends to confirm active tonnage is profitable.

## Formula

```
Vessel Days Idle / Total Vessel Days
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping
- **Sector:** maritime_shipping

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 986 (batch 3)
