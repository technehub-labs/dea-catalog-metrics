# dea:metric-adverse-event-reporting-timeliness

Candidate Performance Metric record for **Adverse Event Reporting Timeliness** (AERT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-adverse-event-reporting-timeliness`
- **Name:** Adverse Event Reporting Timeliness
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AERT

## 2. Definition

Adverse Event Reporting Timeliness (AERT) measures conformance to standards, plans, or obligations in the Pharmaceuticals & Life Sciences domain. The formula is Adverse Reports Filed within Regulatory Deadline / Reports Due - reported in percent (%). It is a standard measure in the Pharmaceuticals sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The speed of submitting safety reports to regulators within required windows - the compliance metric of pharmacovigilance, where timeliness carries legal consequence since reporting deadlines for serious and unexpected events are short, measured in days, and enforced. Its strategic significance is the safety-surveillance system it supports: the entire signal-detection apparatus of post-market safety depends on sponsors reporting on time, which is why timeliness is audited, inspected, and penalized - and why a slipping timeliness rate is treated by inspectors as an indicator of deeper vigilance-system weakness rather than an administrative lapse. The honest read is by report type: serious-window compliance and follow-up-window compliance are different operational problems (case intake versus medical assessment), and lumping them hides which stage of the safety pipeline is degrading.

## Formula

```
Adverse Reports Filed within Regulatory Deadline / Reports Due
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** pharmaceuticals_life_sciences
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 483 (batch 1)
