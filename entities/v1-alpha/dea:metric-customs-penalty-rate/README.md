# dea:metric-customs-penalty-rate

Candidate Performance Metric record for **Customs Penalty Rate** (CPR-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customs-penalty-rate`
- **Name:** Customs Penalty Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CPR-C

## 2. Definition

A International Trade & Customs indicator, Customs Penalty Rate (CPR-C) quantifies exposure to adverse outcomes. Its calculation is Penalty Incidents / Entries Filed, measured in events per thousand or million (scaled). Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. It originates from and is most used in Logistics & Trade practice.

## Formula

```
Penalty Incidents / Entries Filed
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** international_trade_customs
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1710 (batch 6)
