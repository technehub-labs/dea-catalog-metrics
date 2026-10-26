# dea:metric-travel-cost-per-trip

Candidate Performance Metric record for **Travel Cost per Trip** (TCPT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-travel-cost-per-trip`
- **Name:** Travel Cost per Trip
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TCPT

## 2. Definition

Travel Cost per Trip (TCPT) captures how efficiently resources are converted into outputs for organizations tracking corporate travel management. Its calculation is Total Travel Spend / Trips, measured in currency per unit. Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures average fully loaded cost per business trip. It matters because unit cost reveals policy and supplier performance beyond raw spend. Cost can be cut by booking inconvenient travel that degrades traveler productivity and compliance. Read with Traveler Satisfaction (Program) and Policy Compliance Rate (Travel) to confirm savings are humane.

## Formula

```
Total Travel Spend / Trips
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_travel_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1214 (batch 4)
