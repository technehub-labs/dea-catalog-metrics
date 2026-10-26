# dea:metric-average-handle-time-contact-center

Candidate Performance Metric record for **Average Handle Time (Contact Center)** (AHTDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-handle-time-contact-center`
- **Name:** Average Handle Time (Contact Center)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AHTDD

## 2. Definition

Average Handle Time (Contact Center) (AHTDD) captures how efficiently resources are converted into outputs for organizations tracking contact center standard measures (deep dive). It is computed as Talk + Hold + After-Call Work per Contact, expressed in minutes. It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Talk + Hold + After-Call Work per Contact
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4315 (batch 10)
