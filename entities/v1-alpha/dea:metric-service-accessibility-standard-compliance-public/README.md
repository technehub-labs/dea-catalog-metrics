# dea:metric-service-accessibility-standard-compliance-public

Candidate Performance Metric record for **Service Accessibility Standard Compliance (Public)** (SASCP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-accessibility-standard-compliance-public`
- **Name:** Service Accessibility Standard Compliance (Public)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SASCP

## 2. Definition

Service Accessibility Standard Compliance (Public) (SASCP) measures conformance to standards, plans, or obligations in the Public Sector & Citizen Service Standard Measures (Deep Dive) domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Services Meeting Accessibility Obligations / Services - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Public sector sector.

## 3. Context

Measures whether citizen services meet accessibility standards across channels and disabilities. Public services owe accessibility to everyone, with legal force. Compliance measured on digital channels only misses physical and phone access gaps. Read with service accessibility score (Deep Dive) and digital channel adoption (Government) (Deep Dive).

## Formula

```
SASCP = Services Meeting Accessibility Obligations / Services
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** public_sector_citizen_service_standard_measures_deep_dive
- **Sector:** public_sector

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4423 (batch 11)
