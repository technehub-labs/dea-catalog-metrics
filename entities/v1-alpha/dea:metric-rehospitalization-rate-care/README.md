# dea:metric-rehospitalization-rate-care

Candidate Performance Metric record for **Rehospitalization Rate (Care)** (RHR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rehospitalization-rate-care`
- **Name:** Rehospitalization Rate (Care)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RHR

## 2. Definition

Within Elder & Social Care, Rehospitalization Rate (Care) (RHR) is used to gauge the quality of outputs and outcomes. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Rehospitalizations within 30 Days / Discharges - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Social care sector.

## 3. Context

Rehospitalization rate measures residents returning to acute hospital within a window (commonly 30 days) after discharge back to the facility, and it is the system-outcome metric of elder care - payers penalize it, regulators track it, and it is the central quality-of-transitions signal (medication reconciliation, care planning, and early-warning escalation determine whether a deterioration becomes a transfer). The honest measurement distinguishes avoidable from unavoidable returns: some rehospitalizations are appropriate care (end-of-life transfers, acute events no facility can manage), and a rate driven toward zero by under-transfer is a harm, not a quality achievement - the balancing measure is mortality and symptom management. Read with readmission reason taxonomy, avoidable-rate estimates, hospital-to-facility communication completeness, and advance-care-planning coverage which legitimately reduces transfers.

## Formula

```
Rehospitalizations within 30 Days / Discharges
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** elder_social_care
- **Sector:** social_care

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1199 (batch 4)
