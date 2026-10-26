# dea:metric-segregation-of-duties-violation-count

Candidate Performance Metric record for **Segregation of Duties Violation Count** (SODVC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-segregation-of-duties-violation-count`
- **Name:** Segregation of Duties Violation Count
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SODVC

## 2. Definition

Segregation of Duties Violation Count (SODVC) addresses exposure to adverse outcomes and is a fixture of internal controls & financial reporting integrity reporting. The formula is Unresolved SoD Conflicts in Period - reported in count (items per period). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Unresolved SoD Conflicts in Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_controls_financial_reporting_integrity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3577 (batch 8)
