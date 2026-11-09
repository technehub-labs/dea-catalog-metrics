# dea:metric-investment-performance-vs-benchmark-deep-dive

Candidate Performance Metric record for **Investment Performance vs Benchmark (Deep Dive)** (IPVB-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-investment-performance-vs-benchmark-deep-dive`
- **Name:** Investment Performance vs Benchmark (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IPVB-D

## 2. Definition

Investment Performance vs Benchmark (Deep Dive) (IPVB-D) measures how effectively a process or entity achieves its intended outcome in the Asset & Wealth Management (Deep Dive) domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Portfolio Return - Benchmark Return; the result is stated in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. In Financial Services, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures portfolio return against assigned benchmark over standard windows. Benchmark-relative performance is the core accountability metric of professional asset management, and benchmark choice is the honest-read battleground - soft or cherry-picked benchmarks flatter results. Rolling three and five year windows beat point-to-point periods, which start and end dates can game. Read with information ratio (Deep Dive) and alpha generation consistency.

## Formula

```
IPVB-D = Portfolio Return - Benchmark Return
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** asset_wealth_management_deep_dive
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2103 (batch 6)
