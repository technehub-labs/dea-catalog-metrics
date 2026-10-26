# dea:metric-ota-commission-ratio-deep-dive

Candidate Performance Metric record for **OTA Commission Ratio (Deep Dive)** (OTAC-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ota-commission-ratio-deep-dive`
- **Name:** OTA Commission Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OTAC-D

## 2. Definition

OTA Commission Ratio (Deep Dive) (OTAC-D) measures how efficiently resources are converted into outputs in the Hotel & Resort Operations (Deep Dive) domain. The formula is OTA Commissions / Rooms Revenue - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Hospitality sector.

## 3. Context

Measures online travel agency commissions as a share of OTA-booked revenue or total room revenue. It prices the cost of third-party demand, and it has become a board-level topic as commission costs scale with digital intermediation. Ratio movements need volume context: rising commissions with rising total demand can be rational. Read with direct booking ratio (Deep Dive) and channel-mix lifetime value analysis.

## Formula

```
OTA Commissions / Rooms Revenue
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** hotel_resort_operations_deep_dive
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1904 (batch 6)
