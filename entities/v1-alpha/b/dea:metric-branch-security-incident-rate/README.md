# dea:metric-branch-security-incident-rate

Candidate Performance Metric record for **Branch Security Incident Rate** (BSIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-branch-security-incident-rate`
- **Name:** Branch Security Incident Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BSIR

## 2. Definition

Branch Security Incident Rate (BSIR) measures exposure to adverse outcomes in the Retail Banking Branch Network (Deep Dive) domain. It is defined as Security Incidents per Branch per Period; the result is stated in count (items per period). In Banking, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
BSIR = Security Incidents per Branch per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_branch_network_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2124 (batch 6)
