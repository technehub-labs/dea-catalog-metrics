# dea:metric-esg-score-delta-vs-benchmark

Candidate Performance Metric record for **ESG Score Delta vs Benchmark** (ESGSDB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-esg-score-delta-vs-benchmark`
- **Name:** ESG Score Delta vs Benchmark
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ESGSDB

## 2. Definition

ESG Score Delta vs Benchmark (ESGSDB) measures environmental and social sustainability performance in the Investment Performance Measurement domain. The formula is Portfolio ESG Score minus Benchmark ESG Score - reported in score (points). It is a standard measure in the Investment management sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures the portfolio's aggregate ESG score relative to its benchmark. The delta shows whether ESG positioning is intentional or incidental. Third-party scores diverge across providers, making provider choice part of the number. Read with ESG integration coverage in portfolio and active share.

## Formula

```
ESGSDB = Portfolio ESG Score minus Benchmark ESG Score
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** financial
- **Purpose classification:** sustainability
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_performance_measurement
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3456 (batch 7)
