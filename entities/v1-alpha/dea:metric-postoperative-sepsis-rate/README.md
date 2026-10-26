# dea:metric-postoperative-sepsis-rate

Candidate Performance Metric record for **Postoperative Sepsis Rate** (POSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-postoperative-sepsis-rate`
- **Name:** Postoperative Sepsis Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** POSR

## 2. Definition

Postoperative Sepsis Rate (POSR) addresses the quality of outputs and outcomes and is a fixture of healthcare reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Post-Surgical Sepsis Cases / Surgeries; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. In Healthcare, it is a recognized element of the standard performance toolkit.

## 3. Context

Sepsis following surgery, per surgical cases or patient-days - the outcome metric where surgical quality, infection control, and early-recognition systems intersect, since postoperative sepsis is where the consequences of sterile-technique lapses, glycemic control, and delayed recognition all surface together. Its strategic weight is bundled-coverage economics: several surgical-site infection metrics are publicly reported and payment-linked in major systems, and sepsis is the downstream event that converts a wound problem into an ICU stay - which multiplies cost per case by an order of magnitude. Read with the recognition-time companion: sepsis mortality moves sharply with time-to-antibiotics and time-to-source-control, so a hospital's postoperative sepsis rate reflects not only prevention but the rapid-response system catching deterioration early. The case-mix adjustment is the honesty requirement - procedure mix, patient frailty, and elective-versus-emergency status all move expected rates materially.

## Formula

```
Post-Surgical Sepsis Cases / Surgeries
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 474 (batch 1)
