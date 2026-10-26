# dea:metric-defect-escape-rate-deep-dive

Candidate Performance Metric record for **Defect Escape Rate (Deep Dive)** (DER-QA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-defect-escape-rate-deep-dive`
- **Name:** Defect Escape Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DER-QA

## 2. Definition

Defect Escape Rate (Deep Dive) (DER-QA) addresses the quality of outputs and outcomes and is a fixture of software testing & quality engineering reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Defects Found in Production / Total Defects, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of known defects that reach production despite testing. Escapes are the direct measure of quality-gate effectiveness and predict customer-facing disruption. Teams can game it by narrowing what counts as a defect or by suppressing triage of low-severity issues. Read with defect detection rate in testing and escaped defect rate per sprint.

## Formula

```
Defects Found in Production / Total Defects
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** software_testing_quality_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2709 (batch 7)
