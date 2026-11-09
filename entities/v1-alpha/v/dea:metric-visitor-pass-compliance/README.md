# dea:metric-visitor-pass-compliance

Candidate Performance Metric record for **Visitor Pass Compliance** (VPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-visitor-pass-compliance`
- **Name:** Visitor Pass Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** VPC

## 2. Definition

Within Physical Security Operations, Visitor Pass Compliance (VPC) is used to gauge conformance to standards, plans, or obligations. It is defined as Visitors Properly Registered / Visitor Entries Audited; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
VPC = Visitors Properly Registered / Visitor Entries Audited
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** physical_security_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1207 (batch 4)
