# dea:metric-time-to-treatment-for-stroke

Candidate Performance Metric record for **Time to Treatment for Stroke** (TTTS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-treatment-for-stroke`
- **Name:** Time to Treatment for Stroke
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TTTS

## 2. Definition

Time to Treatment for Stroke (TTTS) addresses the quality of outputs and outcomes and is a fixture of healthcare reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Minutes from Arrival to Thrombolysis, measured in minutes. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Healthcare practice.

## 3. Context

Elapsed time from symptom onset or arrival to definitive treatment - the metric where the clinical case for speed is as strong as medicine offers: stroke treatment windows (thrombolysis, thrombectomy) are measured in minutes of salvageable brain tissue, which makes this the canonical door-to-needle interval that emergency systems worldwide publicly benchmark. Its strategic significance is the systems thinking it enforces: the interval spans detection (patient and dispatcher recognition), transport, imaging, and decision - so improvement is never a single-department program but a chain that includes public awareness and prehospital protocols. Read with the decomposition: door-to-needle time is hospital-process speed, onset-to-door is community and emergency-response speed, and different systems fail at different links - which the honest metric reports separately. The obvious gaming risk is clock manipulation, which is why credible programs audit times against source records.

## Formula

```
Minutes from Arrival to Thrombolysis
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
- **Unit label (as published):** minutes

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 473 (batch 1)
