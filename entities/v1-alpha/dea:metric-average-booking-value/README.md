# dea:metric-average-booking-value

Candidate Performance Metric record for **Average Booking Value** (ABV-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-booking-value`
- **Name:** Average Booking Value
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ABV-T

## 2. Definition

Within Travel & Tourism, Average Booking Value (ABV-T) is used to gauge the economic value created or preserved. The formula is Total Booking Revenue / Bookings - reported in currency value. It is a standard measure in the Travel & tourism sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures mean revenue per booking. It matters because travel economics improve via basket depth (ancillaries, add-ons) rather than price alone. Attach pressure at booking can irritate customers and inflate cancellations. Read with Net Promoter Score and Ancillary Revenue per Booking to confirm value growth is welcome.

## Formula

```
ABV-T = Total Booking Revenue / Bookings
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** travel_tourism
- **Sector:** travel_tourism

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 927 (batch 3)
