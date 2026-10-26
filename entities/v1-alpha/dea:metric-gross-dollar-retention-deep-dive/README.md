# dea:metric-gross-dollar-retention-deep-dive

Candidate Performance Metric record for **Gross Dollar Retention (Deep Dive)** (GDRD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gross-dollar-retention-deep-dive`
- **Name:** Gross Dollar Retention (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GDRD

## 2. Definition

Gross Dollar Retention (Deep Dive) (GDRD) measures the retention of customers, users, or assets over time in the Unit Economics & Growth (Deep Dive) domain. The formula is Retained Revenue excluding Expansion / Prior Period - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Software sector.

## 3. Context

Measures recurring revenue retained excluding expansion. GDR isolates the leak: without it, expansion can mask a churning base. GDR computed excluding downgrades overstates retention. Read with net dollar retention (Deep Dive) and logo churn rate (Unit Economics).

## Formula

```
Retained Revenue excluding Expansion / Prior Period
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** unit_economics_growth_deep_dive
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4163 (batch 9)
