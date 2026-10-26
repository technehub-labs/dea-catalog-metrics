# dea:metric-customer-price-sensitivity-uplift-captured

Candidate Performance Metric record for **Customer Price Sensitivity Uplift Captured** (CPSU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-price-sensitivity-uplift-captured`
- **Name:** Customer Price Sensitivity Uplift Captured
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CPSU

## 2. Definition

Customer Price Sensitivity Uplift Captured (CPSU) captures the economic value created or preserved for organizations tracking pricing & revenue management. It is computed as Uplift Realized from Dynamic Pricing / Uplift Modeled, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how much of available willingness-to-pay is actually realized in realized prices. It matters because uncaptured willingness-to-pay is margin left on the table. Estimation models can be tuned to claim large capture that is untestable. Read with Price Realization and Gross Margin trends to confirm modeled capture shows up in financials.

## Formula

```
Uplift Realized from Dynamic Pricing / Uplift Modeled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pricing_revenue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1071 (batch 4)
