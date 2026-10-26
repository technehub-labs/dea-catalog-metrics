# dea:metric-time-to-find-information-deep-dive

Candidate Performance Metric record for **Time to Find Information (Deep Dive)** (TTFI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-find-information-deep-dive`
- **Name:** Time to Find Information (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TTFI

## 2. Definition

Time to Find Information (Deep Dive) (TTFI) addresses how efficiently resources are converted into outputs and is a fixture of knowledge management (deep dive) reporting. It is a working-level control: thresholds trigger immediate operational response. It is defined as Median Minutes to Locate Required Knowledge; the result is stated in minutes. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
TTFI = Median Minutes to Locate Required Knowledge
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** knowledge_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3917 (batch 8)
