# dea:metric-menu-item-margin-mix

Candidate Performance Metric record for **Menu Item Margin Mix** (MIM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-menu-item-margin-mix`
- **Name:** Menu Item Margin Mix
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MIM

## 2. Definition

Menu Item Margin Mix (MIM) addresses the economic value created or preserved and is a fixture of restaurants reporting. It is computed as Contribution Margin of Items Sold / Total Menu Margin Potential, expressed in percent (%). Its use is concentrated in Restaurants. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the proportion of high-margin items in total sales mix in restaurants. It matters because mix engineering is the strongest lever on restaurant profitability. Pushing high-margin items can narrow the menu appeal and hurt traffic. Read with Average Check and Item Popularity Index to confirm mix optimization serves guests.

## Formula

```
Contribution Margin of Items Sold / Total Menu Margin Potential
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** restaurants
- **Sector:** restaurants

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 940 (batch 3)
