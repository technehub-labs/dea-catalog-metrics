# dea:metric-circular-material-use-rate

Candidate Performance Metric record for **Circular Material Use Rate** (CMUR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-circular-material-use-rate`
- **Name:** Circular Material Use Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CMUR

## 2. Definition

Circular Material Use Rate (CMUR) addresses environmental and social sustainability performance and is a fixture of sustainability & esg reporting. Its calculation is Secondary Materials / Total Materials Used, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of material inputs that come from recycled or reused sources - the circular-economy metric that measures the demand side of recycling: how much of what the organization builds is built from material that has already had a life. Its strategic significance is dependency inversion: recycled feedstock reduces virgin extraction exposure, and in materials facing supply constraints the secondary stream is a resilience asset as much as a sustainability one. The measurement complications are quality and accounting - recycled content claims rest on supplier certification chains with variable rigor, and mass-balance accounting (allocating recycled input across outputs proportionally) is the convention that lets the number be quoted at all. Read with the recyclability counterpart: high recyclability with low recycled content describes an industry that designs well and sources virgin; closing the loop requires both numbers to move.

## Formula

```
CMUR = Secondary Materials / Total Materials Used
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 428 (batch 1)
