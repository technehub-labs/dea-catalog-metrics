# dea:metric-idle-time-ratio-contact-center

Candidate Performance Metric record for **Idle Time Ratio (Contact Center)** (ITR-CC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-idle-time-ratio-contact-center`
- **Name:** Idle Time Ratio (Contact Center)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ITR-CC

## 2. Definition

Idle Time Ratio (Contact Center) (ITR-CC) addresses how efficiently resources are converted into outputs and is a fixture of contact center standard measures (deep dive) reporting. It is a working-level control: thresholds trigger immediate operational response. It is defined as Unproductive Waiting Time / Paid Time; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Unproductive Waiting Time / Paid Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4334 (batch 10)
