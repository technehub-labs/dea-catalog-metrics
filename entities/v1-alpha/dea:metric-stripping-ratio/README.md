# dea:metric-stripping-ratio

Candidate Performance Metric record for **Stripping Ratio** (STR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-stripping-ratio`
- **Name:** Stripping Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** STR

## 2. Definition

Stripping Ratio (STR) captures how efficiently resources are converted into outputs for organizations tracking mining & metals. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Waste Rock Removed / Ore Extracted, measured in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Mining & metals practice.

## 3. Context

The stripping ratio is the tonnes of waste removed per tonne of ore mined, the defining cost lever of open-pit operations. A low ratio keeps unit costs near the floor; as pits deepen, ratios climb mechanically, which is why strip-ratio trajectory is the standard way to test whether a mine plan is credible or deferring hard waste movement. Gaming risk is real: mining higher-grade pockets to keep the ratio flattering can unbalance the schedule and trigger a cost step-change later. Read it with reserve depth staging and the mine plan's year-by-year profile, not just the current period.

## Formula

```
Waste Rock Removed / Ore Extracted
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** mining_metals
- **Sector:** mining_metals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 716 (batch 2)
