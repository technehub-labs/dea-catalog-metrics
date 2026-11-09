# dea:metric-internal-fill-rate

Candidate Performance Metric record for **Internal Fill Rate** (IFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-internal-fill-rate`
- **Name:** Internal Fill Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IFR

## 2. Definition

A Human Resources indicator, Internal Fill Rate (IFR) quantifies capability maturity or development. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Positions Filled Internally / Total Positions Filled, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of vacancies filled by internal candidates. It matters because it reflects succession depth, retention economics, and whether development promises are real. Teams can inflate it by posting roles only internally first or discouraging external competition. Read with Employee Engagement Score and Time to Fill to confirm internal mobility is opportunity, not constraint.

## Formula

```
IFR = Positions Filled Internally / Total Positions Filled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 141 (batch 1)
