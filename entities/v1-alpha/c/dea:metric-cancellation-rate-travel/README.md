# dea:metric-cancellation-rate-travel

Candidate Performance Metric record for **Cancellation Rate (Travel)** (CNL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cancellation-rate-travel`
- **Name:** Cancellation Rate (Travel)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CNL

## 2. Definition

Within Travel & Tourism, Cancellation Rate (Travel) (CNL) is used to gauge exposure to adverse outcomes. It is computed as Cancelled Bookings / Total Bookings, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is concentrated in Travel & tourism.

## 3. Context

Measures the share of bookings later cancelled. It matters because cancellations destroy forecast revenue and force overbooking responses. Non-refundable pricing suppresses cancellations but damages conversion and satisfaction. Read with Booking Conversion Rate (Travel) and Customer Lifetime Value to confirm cancellation policy balances yield and trust.

## Formula

```
CNL = Cancelled Bookings / Total Bookings
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** travel_tourism
- **Sector:** travel_tourism

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 930 (batch 3)
