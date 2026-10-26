# dea:metric-average-billing-rate

Candidate Performance Metric record for **Average Billing Rate** (ABR-PS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-billing-rate`
- **Name:** Average Billing Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ABR-PS

## 2. Definition

Average Billing Rate (ABR-PS) measures the economic value created or preserved in the Professional Services domain. It is defined as Fee Revenue / Billable Hours; the result is stated in currency per unit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Professional services, it is a recognized element of the standard performance toolkit.

## 3. Context

Revenue per billed hour - the pricing metric of professional services, and the complement to utilization in the revenue identity: revenue equals billable hours times rate, so the two levers are multiplicative, and pricing moves revenue without requiring anyone to work longer. Its strategic significance is the value-pricing debate it participates in: the billable-hour model is under sustained pressure from clients who want outcomes priced rather than inputs, and the average-rate trend reveals whether the firm is escaping it - through specialization, value-based fee structures, or premium positioning - or competing on time. The honest read is realization-adjusted: standard rates minus discounts, write-downs, and non-billable time is what was actually earned, and the gap between standard and realized rate is the pricing-discipline story. Read by level and service line: rate trends by role show where premium is actually earned, while blended rates move with mix and hide deterioration inside a stable headline.

## Formula

```
Fee Revenue / Billable Hours
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** professional_services
- **Sector:** professional_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 679 (batch 2)
