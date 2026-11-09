# dea:metric-central-line-associated-bloodstream-infection-rate

Candidate Performance Metric record for **Central Line-Associated Bloodstream Infection Rate** (CLABSI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-central-line-associated-bloodstream-infection-rate`
- **Name:** Central Line-Associated Bloodstream Infection Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CLABSI

## 2. Definition

A Healthcare Quality & Patient Safety Standard Measures indicator, Central Line-Associated Bloodstream Infection Rate (CLABSI) quantifies exposure to adverse outcomes. The formula is CLABSI Events / 1,000 Central Line Days - reported in events per thousand or million (scaled). It is a standard measure in the Healthcare sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures CLABSI events per line-day. These infections are largely preventable and treated as a proxy for care discipline. Surveillance intensity affects detection independent of true incidence. Read with hand hygiene compliance rate and catheter-associated urinary tract infection rate.

## Formula

```
CLABSI = CLABSI Events / 1,000 Central Line Days
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** healthcare_quality_patient_safety_standard_measures
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4239 (batch 10)
