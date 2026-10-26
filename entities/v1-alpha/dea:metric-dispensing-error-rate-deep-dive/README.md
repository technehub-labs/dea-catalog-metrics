# dea:metric-dispensing-error-rate-deep-dive

Candidate Performance Metric record for **Dispensing Error Rate (Deep Dive)** (DER-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dispensing-error-rate-deep-dive`
- **Name:** Dispensing Error Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DER-D

## 2. Definition

Dispensing Error Rate (Deep Dive) (DER-D) captures exposure to adverse outcomes for organizations tracking pharmacy retail. The formula is Dispensing Errors / Prescriptions Dispensed - reported in events per thousand or million (scaled). It is a standard measure in the Healthcare sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures errors in prescription dispensing - wrong drug, strength, label, or patient - per prescription filled. It is the patient-safety core of pharmacy operations, where volume and speed pressure create error conditions, and reported rates historically underestimate true rates. Error classification and near-miss capture determine credibility, since a zero rate usually means zero detection. Read with barcode-verification coverage and pharmacist workload-per-hour thresholds.

## Formula

```
Dispensing Errors / Prescriptions Dispensed
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** pharmacy_retail
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2285 (batch 6)
