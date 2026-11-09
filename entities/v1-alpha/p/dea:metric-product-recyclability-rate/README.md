# dea:metric-product-recyclability-rate

Candidate Performance Metric record for **Product Recyclability Rate** (PRR2) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-product-recyclability-rate`
- **Name:** Product Recyclability Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PRR2

## 2. Definition

Product Recyclability Rate (PRR2) captures environmental and social sustainability performance for organizations tracking sustainability & esg. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Recyclable Product Mass / Total Product Mass, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The share of product mass designed to be recyclable at end of life - the design-stage circularity metric that distinguishes what a product could become from what actually happens to it, a distinction that is both its strategic value and its gaming risk. Regulation increasingly targets exactly this attribute: eco-design and right-to-repair regimes set recyclability thresholds and recycled-content requirements, which converts the metric from a marketing claim into a compliance parameter with design consequence - recyclability is decided in the first weeks of product design and cannot be retrofitted. The honest version carries disclaimers: recyclability depends on infrastructure that varies by region, and a theoretically recyclable product in a market without collection systems is recyclable on paper only. Read with the actual recycled-content rate: designing for recycling and building from recycled material are separate circularity claims, and the gap between them describes the industry's actual state.

## Formula

```
PRR2 = Recyclable Product Mass / Total Product Mass
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** sustainability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** sustainability_esg

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 426 (batch 1)
