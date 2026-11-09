# dea:metric-code-duplication-rate

Candidate Performance Metric record for **Code Duplication Rate** (CDR-SA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-code-duplication-rate`
- **Name:** Code Duplication Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDR-SA

## 2. Definition

Code Duplication Rate (CDR-SA) captures the quality of outputs and outcomes for organizations tracking software architecture & technical design. It provides the day-to-day signal that a process is running as designed. Its calculation is Duplicated Lines / Total Lines, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
CDR-SA = Duplicated Lines / Total Lines
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_architecture_technical_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2624 (batch 7)
