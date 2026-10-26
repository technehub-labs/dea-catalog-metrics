# dea:metric-device-survival-rate

Candidate Performance Metric record for **Device Survival Rate** (DSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-device-survival-rate`
- **Name:** Device Survival Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DSR

## 2. Definition

Device Survival Rate (DSR) captures the quality of outputs and outcomes for organizations tracking medical devices. It is defined as Devices Functioning at Time Point / Devices Implanted; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Medical devices, it is a recognized element of the standard performance toolkit.

## 3. Context

Device survival rate is the actuarial heart of the medical device industry - the estimated share of devices still functioning at 1, 3, or 5 years post-implant, and it is the single most important disclosure in premarket approval submissions to FDA. For implantables, survival analysis shapes regulatory clearance, product-liability exposure, and replacement-market sizing simultaneously. The measurement complexity is real: it depends on the number of devices still under observation, and censoring (patients lost to follow-up) must be handled with proper statistical techniques, not simple ratios. Read with warranty cost and complaint rate for triangulation, and with revision burden for the surgical-system view.

## Formula

```
Devices Functioning at Time Point / Devices Implanted
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_devices
- **Sector:** medical_devices

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 759 (batch 2)
