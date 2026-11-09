# dea:metric-mdm-platform-availability

Candidate Performance Metric record for **MDM Platform Availability** (MDMPA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mdm-platform-availability`
- **Name:** MDM Platform Availability
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MDMPA

## 2. Definition

A Master Data Management indicator, MDM Platform Availability (MDMPA) quantifies the quality of outputs and outcomes. It is computed as Uptime of MDM Hub Services, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
MDMPA = Uptime of MDM Hub Services
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** master_data_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3650 (batch 8)
