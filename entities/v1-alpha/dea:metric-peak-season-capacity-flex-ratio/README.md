# dea:metric-peak-season-capacity-flex-ratio

Candidate Performance Metric record for **Peak Season Capacity Flex Ratio** (PSCF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-peak-season-capacity-flex-ratio`
- **Name:** Peak Season Capacity Flex Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PSCF

## 2. Definition

A Parcel & Last-Mile Logistics (Deep Dive) indicator, Peak Season Capacity Flex Ratio (PSCF) quantifies the utilization or availability of capacity. It is computed as Peak Volume Handled / Baseline Capacity, expressed in ratio (x:1 or x). Its use is concentrated in Logistics & Trade. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures peak-to-average capacity and the flex capability (temporary drivers, rented vehicles, overflow networks) covering the peak. Peak-season economics decide parcel profitability: fixed networks sized for peak are ruinous, and under-flexed peaks fail customers at the highest-volume, highest-loyalty-risk moment. The ratio must be tested against realistic peak forecasts, not last year's actual. Read with peak service performance and cost per parcel (Deep Dive) seasonality.

## Formula

```
Peak Volume Handled / Baseline Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** parcel_last_mile_logistics_deep_dive
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2343 (batch 6)
