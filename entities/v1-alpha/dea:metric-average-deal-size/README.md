# dea:metric-average-deal-size

Candidate Performance Metric record for **Average Deal Size** (ADS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-deal-size`
- **Name:** Average Deal Size
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ADS

## 2. Definition

Average Deal Size (ADS) captures the economic value created or preserved for organizations tracking sales. It is computed as Total Closed Revenue / Closed Deals, expressed in currency value. It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the mean value of closed deals in a period. It matters because it links sales effort to revenue economics and shapes capacity planning. Gaming risk includes pulling a few mega-deals into the period to lift the average, or splitting deals to manage quota credit. Read with Upsell Revenue Ratio and Win Rate to see whether larger deals are closing at healthy rates or just dragging cycles.

## Formula

```
Total Closed Revenue / Closed Deals
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 91 (batch 1)
