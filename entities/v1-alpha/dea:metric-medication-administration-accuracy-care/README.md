# dea:metric-medication-administration-accuracy-care

Candidate Performance Metric record for **Medication Administration Accuracy (Care)** (MAAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-medication-administration-accuracy-care`
- **Name:** Medication Administration Accuracy (Care)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MAAC

## 2. Definition

Within Elder & Social Care, Medication Administration Accuracy (Care) (MAAC) is used to gauge the quality of outputs and outcomes. It is computed as Correct Administrations Observed / Administrations Observed, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Social care.

## 3. Context

Medication administration accuracy measures error-free administration against total administrations, and in elder care it is the highest-severity process-safety metric - the population carries polypharmacy (many residents take a dozen or more medications), cognitive impairment that prevents error self-detection, and frailty that magnifies consequence. The safety-science reading matters: administration error rates measured by direct observation exceed self-reported and incident-report-based rates by an order of magnitude, so the measurement method determines the number, and voluntary reporting undercounts systematically. The intervention evidence is well established: barcode medication administration and pharmacist review reduce error rates substantially, and the error taxonomy (wrong drug, dose, time, route, patient) determines which fix applies. Read with high-alert medication error frequency specifically, error-severity distribution, near-miss catch rate, and reconciliation-at-transition coverage since errors concentrate at care handoffs.

## Formula

```
Correct Administrations Observed / Administrations Observed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** elder_social_care
- **Sector:** social_care

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1195 (batch 4)
