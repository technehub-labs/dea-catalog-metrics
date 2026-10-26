# dea:metric-suitability-review-completion

Candidate Performance Metric record for **Suitability Review Completion** (SRC-W) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-suitability-review-completion`
- **Name:** Suitability Review Completion
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SRC-W

## 2. Definition

Within Wealth Management, Suitability Review Completion (SRC-W) is used to gauge conformance to standards, plans, or obligations. Its calculation is Client Files Reviewed within Cycle / Client Files, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Wealth management practice.

## 3. Context

Suitability review completion measures adherence to the regulatory obligation to verify that recommendations fit a client's objectives, risk tolerance, and financial situation - the core conduct requirement in wealth under regimes like MiFID II and FINRA suitability rules. It is the compliance-infrastructure metric where failure is direct enforcement exposure: suitability breaches are among the most common disciplinary findings in wealth management, with fines and restitution following. The honest version measures quality of the review, not just checkbox completion: evidence-of-understanding documentation, risk-profiling updates after life events, and concentration checks are where substance lives. Read with complaint root-cause analysis (suitability complaints surface failures the process missed), supervisory review depth, and profiling-refresh currency by client age cohort.

## Formula

```
Client Files Reviewed within Cycle / Client Files
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** wealth_management
- **Sector:** wealth_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1139 (batch 4)
