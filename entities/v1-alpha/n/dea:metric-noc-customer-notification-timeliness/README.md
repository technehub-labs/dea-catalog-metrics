# dea:metric-noc-customer-notification-timeliness

Candidate Performance Metric record for **NOC Customer Notification Timeliness** (NCNT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-noc-customer-notification-timeliness`
- **Name:** NOC Customer Notification Timeliness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NCNT

## 2. Definition

NOC Customer Notification Timeliness (NCNT) measures the quality of outputs and outcomes in the Network Operations Center (Deep Dive) domain. It is computed as Outage Notifications Sent within Commitment / Outages, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
NCNT = Outage Notifications Sent within Commitment / Outages
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** network_operations_center_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2853 (batch 7)
