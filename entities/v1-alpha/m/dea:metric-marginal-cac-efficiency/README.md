# dea:metric-marginal-cac-efficiency

Candidate Performance Metric record for **Marginal CAC Efficiency** (MCAE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-marginal-cac-efficiency`
- **Name:** Marginal CAC Efficiency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MCAE

## 2. Definition

A Unit Economics & Growth (Deep Dive) indicator, Marginal CAC Efficiency (MCAE) quantifies how efficiently resources are converted into outputs. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Change in Customers / Change in Acquisition Spend - reported in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Software sector.

## 3. Context

Measures how acquisition cost behaves as spend scales. Marginal efficiency is where growth economics actually break: the last dollar of paid acquisition is the worst. Efficiency measured on blended rather than incremental spend hides the decay. Read with LTV-to-CAC ratio (Deep Dive) and customer acquisition cost trend (Deep Dive).

## Formula

```
MCAE = Change in Customers / Change in Acquisition Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** unit_economics_growth_deep_dive
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4167 (batch 9)
