# dea:metric-ore-grade

Candidate Performance Metric record for **Ore Grade** (OG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ore-grade`
- **Name:** Ore Grade
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OG

## 2. Definition

Ore Grade (OG) measures the quality of outputs and outcomes in the Mining & Metals domain. Its calculation is Metal Content / Ore Extracted, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Mining & metals practice.

## 3. Context

Ore grade is the metal content of mined rock, expressed as grams per tonne or percent, and it is the single biggest geological driver of a mine's economics - grade times tonnage sets revenue before a single cost decision is made. High-grade ore lowers the cost per unit of metal and widens margins; declining grades across mature districts are why sector-wide cost curves have crept upward for two decades. Read it against reserves life and cutoff grade policy, because a mine can flatter near-term grade by mining selectively and starving the future. Pair with All-In Sustaining Cost to see the full margin picture.

## Formula

```
Metal Content / Ore Extracted
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** mining_metals
- **Sector:** mining_metals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 714 (batch 2)
