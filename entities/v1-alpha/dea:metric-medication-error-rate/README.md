# dea:metric-medication-error-rate

Candidate Performance Metric record for **Medication Error Rate** (MER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-medication-error-rate`
- **Name:** Medication Error Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MER

## 2. Definition

Within Healthcare, Medication Error Rate (MER) is used to gauge exposure to adverse outcomes. Its calculation is Medication Errors / Medication Administrations, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. It originates from and is most used in Healthcare practice.

## 3. Context

Errors in prescribing, dispensing, or administration of medication, normalized per thousand doses or orders - the safety metric that healthcare's human-factors tradition treats as the archetypal systems problem, since the research (beginning with the landmark harm studies) showed medication error is rarely carelessness and usually process design. Its strategic weight is the double counting problem: errors with harm and errors caught before harm are the same metric family, and safe systems are those that catch errors upstream - which means a rising error rate after reporting-safety culture improves can mean better detection rather than worse care. Read with the severity taxonomy: near-miss and no-harm errors are the learning signal, harm errors are the outcome signal, and the ratio between them describes the system's defenses. The interventions this metric steers - computerized order entry, barcode administration, pharmacist review - are the best-evidenced safety investments in the field.

## Formula

```
Medication Errors / Medication Administrations
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** healthcare
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 471 (batch 1)
