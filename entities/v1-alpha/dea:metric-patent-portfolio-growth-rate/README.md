# dea:metric-patent-portfolio-growth-rate

Candidate Performance Metric record for **Patent Portfolio Growth Rate** (PPGR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-patent-portfolio-growth-rate`
- **Name:** Patent Portfolio Growth Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PPGR

## 2. Definition

Patent Portfolio Growth Rate (PPGR) captures growth over time for organizations tracking intellectual property & licensing. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Net New Patents Filed per Period, measured in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the pace of expansion of the patent estate. Portfolio growth is the quantitative signal of innovation being captured as property. Filing volume incentivized without quality fills the portfolio with low-value assets. Read with patent grant success rate and IP value realization rate.

## Formula

```
PPGR = Net New Patents Filed per Period
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** growth
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** intellectual_property_licensing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3935 (batch 8)
