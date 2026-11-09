# dea:metric-roaming-revenue-per-user

Candidate Performance Metric record for **Roaming Revenue per User** (RRPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-roaming-revenue-per-user`
- **Name:** Roaming Revenue per User
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RRPU

## 2. Definition

Roaming Revenue per User (RRPU) captures the economic value created or preserved for organizations tracking telecom product & bundle management. Its calculation is Roaming Revenue / Roaming-Eligible Subscribers, measured in currency per unit. Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Telecommunications practice.

## 3. Context

Measures roaming revenue per roaming or traveling subscriber. It matters because roaming is a high-margin overlay on core subscriptions. Gaming risk includes selling roaming add-ons that customers forget to cancel. Read with Roaming Complaint Rate and add-on utilization to confirm revenue is earned, not trapped.

## Formula

```
RRPU = Roaming Revenue / Roaming-Eligible Subscribers
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecom_product_bundle_management
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1445 (batch 5)
