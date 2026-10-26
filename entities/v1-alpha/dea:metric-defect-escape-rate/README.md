# dea:metric-defect-escape-rate

Candidate Performance Metric record for **Defect Escape Rate** (DER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-defect-escape-rate`
- **Name:** Defect Escape Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DER

## 2. Definition

Defect Escape Rate (DER) addresses the quality of outputs and outcomes and is a fixture of software engineering reporting. It is defined as Defects Found in Production / Total Defects Found; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of defects that reach production or customers instead of being caught earlier. It matters because escaped defects cost orders of magnitude more than caught ones. Teams can shrink it cosmetically by softening production incident classifications or widening what counts as expected behavior. Read with Defect Density and Mean Time to Detect to confirm fewer escapes reflect better testing, not looser definitions.

## Formula

```
Defects Found in Production / Total Defects Found
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 286 (batch 1)
