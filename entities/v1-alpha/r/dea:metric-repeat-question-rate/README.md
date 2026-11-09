# dea:metric-repeat-question-rate

Candidate Performance Metric record for **Repeat Question Rate** (RQR-KM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-repeat-question-rate`
- **Name:** Repeat Question Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RQR-KM

## 2. Definition

Repeat Question Rate (RQR-KM) captures the quality of outputs and outcomes for organizations tracking knowledge management (deep dive). It provides the day-to-day signal that a process is running as designed. Its calculation is Questions Asked That Have Existing Answers / Questions, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
RQR-KM = Questions Asked That Have Existing Answers / Questions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3929 (batch 8)
