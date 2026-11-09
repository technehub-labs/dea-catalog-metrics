# dea:metric-repeat-finding-rate-compliance

Candidate Performance Metric record for **Repeat Finding Rate (Compliance)** (RFRC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-repeat-finding-rate-compliance`
- **Name:** Repeat Finding Rate (Compliance)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RFRC

## 2. Definition

Repeat Finding Rate (Compliance) (RFRC) measures the quality of outputs and outcomes in the Compliance Monitoring & Testing domain. It is computed as Findings Recurring from Prior Cycle / Findings, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
RFRC = Findings Recurring from Prior Cycle / Findings
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** compliance_monitoring_testing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3559 (batch 8)
