# dea:metric-preferred-supplier-share-travel

Candidate Performance Metric record for **Preferred Supplier Share (Travel)** (PSS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-preferred-supplier-share-travel`
- **Name:** Preferred Supplier Share (Travel)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PSS

## 2. Definition

Within Corporate Travel Management, Preferred Supplier Share (Travel) (PSS) is used to gauge the economic value created or preserved. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Bookings with Preferred Suppliers / Total Bookings, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of travel spend going through preferred suppliers. It matters because supplier consolidation is what earns negotiated rates and service tiers. Share can be inflated by mandating suppliers regardless of trip economics. Read with Travel Cost per Trip and Policy Compliance Rate (Travel) to confirm consolidation pays.

## Formula

```
PSS = Bookings with Preferred Suppliers / Total Bookings
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_travel_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1217 (batch 4)
