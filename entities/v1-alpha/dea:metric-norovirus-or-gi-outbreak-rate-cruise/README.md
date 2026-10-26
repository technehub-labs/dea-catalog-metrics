# dea:metric-norovirus-or-gi-outbreak-rate-cruise

Candidate Performance Metric record for **Norovirus or GI Outbreak Rate (Cruise)** (GIOR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-norovirus-or-gi-outbreak-rate-cruise`
- **Name:** Norovirus or GI Outbreak Rate (Cruise)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GIOR

## 2. Definition

Norovirus or GI Outbreak Rate (Cruise) (GIOR) captures exposure to adverse outcomes for organizations tracking cruise & passenger shipping. The formula is Outbreak Voyages / Voyages - reported in events per thousand or million (scaled). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Hospitality sector.

## 3. Context

Measures gastrointestinal illness incidence against public-health thresholds that trigger CDC and port-health reporting. Outbreaks are the reputational nightmare of cruising - single events have moved fleet-wide demand - making this both a hygiene metric and a demand-side risk metric. Case definitions and reporting thresholds are standardized, so comparisons are meaningful. Read with sanitation inspection scores and provisioning hygiene audits.

## Formula

```
GIOR = Outbreak Voyages / Voyages
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cruise_passenger_shipping
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1928 (batch 6)
