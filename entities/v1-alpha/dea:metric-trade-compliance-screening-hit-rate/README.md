# dea:metric-trade-compliance-screening-hit-rate

Candidate Performance Metric record for **Trade Compliance Screening Hit Rate** (TCSH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-trade-compliance-screening-hit-rate`
- **Name:** Trade Compliance Screening Hit Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TCSH

## 2. Definition

Trade Compliance Screening Hit Rate (TCSH) measures exposure to adverse outcomes in the International Trade & Customs domain. It is defined as Denied-Party Hits Confirmed / Screening Hits; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. In Logistics & Trade, it is a recognized element of the standard performance toolkit.

## Formula

```
TCSH = Denied-Party Hits Confirmed / Screening Hits
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** international_trade_customs
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1714 (batch 6)
