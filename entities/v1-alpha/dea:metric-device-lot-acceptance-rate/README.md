# dea:metric-device-lot-acceptance-rate

Candidate Performance Metric record for **Device Lot Acceptance Rate** (DLAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-device-lot-acceptance-rate`
- **Name:** Device Lot Acceptance Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DLAR

## 2. Definition

A Medical Devices indicator, Device Lot Acceptance Rate (DLAR) quantifies the quality of outputs and outcomes. It is defined as Lots Accepted on Release Testing / Lots Tested; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. In Medical devices, it is a recognized element of the standard performance toolkit.

## Formula

```
Lots Accepted on Release Testing / Lots Tested
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
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_devices
- **Sector:** medical_devices

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 755 (batch 2)
