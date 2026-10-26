# dea:metric-channel-inventory-weeks-of-cover

Candidate Performance Metric record for **Channel Inventory Weeks of Cover** (CIWOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-channel-inventory-weeks-of-cover`
- **Name:** Channel Inventory Weeks of Cover
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CIWOC

## 2. Definition

Channel Inventory Weeks of Cover (CIWOC) addresses the utilization or availability of capacity and is a fixture of channel & distribution management reporting. It is defined as Partner Inventory on Hand / Weekly Sell-Through; the result is stated in weeks. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
CIWOC = Partner Inventory on Hand / Weekly Sell-Through
```

## Unit

- **Unit reference:** `dea:unit-week`
- **Unit:** week
- **Unit label (as published):** weeks

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** channel_distribution_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3980 (batch 8)
