# dea:metric-loyalty-member-stay-share-deep-dive

Candidate Performance Metric record for **Loyalty Member Stay Share (Deep Dive)** (LMSS-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-loyalty-member-stay-share-deep-dive`
- **Name:** Loyalty Member Stay Share (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LMSS-D

## 2. Definition

Loyalty Member Stay Share (Deep Dive) (LMSS-D) measures the retention of customers, users, or assets over time in the Hotel & Resort Operations (Deep Dive) domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Loyalty Room Nights / Total Room Nights, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Hospitality practice.

## 3. Context

Measures the share of room nights from program members. It is the strategic distribution metric of hotel brands: members book direct, cost less to acquire, and concentrate their stays where programs reward them. Beware share inflated by points promos that attract deal-seekers rather than loyal behavior. Read with member repeat frequency and direct booking ratio (Deep Dive).

## Formula

```
LMSS-D = Loyalty Room Nights / Total Room Nights
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
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** hotel_resort_operations_deep_dive
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1910 (batch 6)
