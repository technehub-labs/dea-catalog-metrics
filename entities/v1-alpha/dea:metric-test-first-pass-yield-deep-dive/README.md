# dea:metric-test-first-pass-yield-deep-dive

Candidate Performance Metric record for **Test First Pass Yield (Deep Dive)** (TFPY-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-test-first-pass-yield-deep-dive`
- **Name:** Test First Pass Yield (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TFPY-D

## 2. Definition

Within Semiconductor Manufacturing (Deep Dive), Test First Pass Yield (Deep Dive) (TFPY-D) is used to gauge the quality of outputs and outcomes. Its calculation is Units Passing Final Test First Time / Units Tested, measured in percent (%). It originates from and is most used in Semiconductors practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures devices passing final test on the first attempt. It is the final quality gate of semiconductor manufacturing, and failures here carry the full cost of the wafer - every retest or scrap is sunk capital lost. First-pass yield improvements from loosening test limits convert fab quality into field failures and customer returns, so limit changes need governance. Read with die yield (Deep Dive) and customer return and reliability data.

## Formula

```
Units Passing Final Test First Time / Units Tested
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** semiconductor_manufacturing_deep_dive
- **Sector:** semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2379 (batch 6)
