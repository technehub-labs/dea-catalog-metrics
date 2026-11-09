# dea:metric-contract-sla-attainment-cleaning

Candidate Performance Metric record for **Contract SLA Attainment (Cleaning)** (CSLA-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contract-sla-attainment-cleaning`
- **Name:** Contract SLA Attainment (Cleaning)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CSLA-C

## 2. Definition

Contract SLA Attainment (Cleaning) (CSLA-C) measures conformance to standards, plans, or obligations in the Cleaning & Environmental Services domain. The formula is SLAs Met / SLAs Measured - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Facility Services sector.

## Formula

```
CSLA-C = SLAs Met / SLAs Measured
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** cleaning_environmental_services
- **Sector:** facility_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2048 (batch 6)
