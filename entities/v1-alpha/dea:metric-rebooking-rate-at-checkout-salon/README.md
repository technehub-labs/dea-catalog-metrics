# dea:metric-rebooking-rate-at-checkout-salon

Candidate Performance Metric record for **Rebooking Rate at Checkout (Salon)** (RRC-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rebooking-rate-at-checkout-salon`
- **Name:** Rebooking Rate at Checkout (Salon)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RRC-S

## 2. Definition

Within Beauty & Personal Care Services, Rebooking Rate at Checkout (Salon) (RRC-S) is used to gauge the retention of customers, users, or assets over time. Its calculation is Appointments Booked before Leaving / Appointments Served, measured in percent (%). It originates from and is most used in Personal Services practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of service appointments that end with the next visit booked before the client leaves. It is the single highest-leverage retention behavior in personal services: pre-booked clients churn far less and fill chairs predictably, and walk-off clients often never return. Front-desk scripting and stylist recommendation quality move this rate. Read with client return interval trends and no-show rates on pre-booked visits.

## Formula

```
Appointments Booked before Leaving / Appointments Served
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** beauty_personal_care_services
- **Sector:** personal_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2020 (batch 6)
