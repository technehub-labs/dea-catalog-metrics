# dea:metric-mortality-within-30-days-of-procedure

Candidate Performance Metric record for **Mortality within 30 Days of Procedure** (MP30) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mortality-within-30-days-of-procedure`
- **Name:** Mortality within 30 Days of Procedure
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MP30

## 2. Definition

Within Veterinary & Animal Health, Mortality within 30 Days of Procedure (MP30) is used to gauge exposure to adverse outcomes. It is defined as Deaths within 30 Days / Procedures; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. In Healthcare, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures deaths within thirty days of surgical or medical intervention. It is the gravest outcome metric in veterinary care, combining surgical skill, anesthesia quality, and case selection. Small denominators per clinic make rates noisy, so aggregate by procedure class across periods, and risk-adjust for ASA status and age. Read with surgical complication rate (Vet) and informed-consent documentation compliance.

## Formula

```
Deaths within 30 Days / Procedures
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** veterinary_animal_health
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2039 (batch 6)
