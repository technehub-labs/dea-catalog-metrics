# dea:metric-availability-zone-redundancy-compliance

Candidate Performance Metric record for **Availability Zone Redundancy Compliance** (AZRC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-availability-zone-redundancy-compliance`
- **Name:** Availability Zone Redundancy Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AZRC

## 2. Definition

Availability Zone Redundancy Compliance (AZRC) measures exposure to adverse outcomes in the Observability & Site Reliability Engineering domain. The formula is Services Meeting Redundancy Standard / Services - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of critical services deployed across multiple availability zones per architecture standards. Zone redundancy is what converts a data-center event from an outage into a non-event. Compliance without regular zone-failover testing is unverified redundancy. Read with chaos experiment execution rate and service level objective attainment.

## Formula

```
Services Meeting Redundancy Standard / Services
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2864 (batch 7)
