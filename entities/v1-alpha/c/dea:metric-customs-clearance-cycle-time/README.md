# dea:metric-customs-clearance-cycle-time

Candidate Performance Metric record for **Customs Clearance Cycle Time** (CCCT-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customs-clearance-cycle-time`
- **Name:** Customs Clearance Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CCCT-T

## 2. Definition

Customs Clearance Cycle Time (CCCT-T) addresses how efficiently resources are converted into outputs and is a fixture of international trade & customs reporting. Its calculation is Hours from Arrival to Customs Release, measured in hours. It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Logistics & Trade practice.

## Formula

```
CCCT-T = Hours from Arrival to Customs Release
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** international_trade_customs
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1706 (batch 6)
