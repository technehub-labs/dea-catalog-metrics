# dea:metric-statement-of-account-accuracy

Candidate Performance Metric record for **Statement of Account Accuracy** (SOAA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-statement-of-account-accuracy`
- **Name:** Statement of Account Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SOAA

## 2. Definition

Statement of Account Accuracy (SOAA) addresses the quality of outputs and outcomes and is a fixture of insurance distribution & brokerage reporting. It is defined as Accurate Commission Statements / Statements Issued; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. In Insurance distribution, it is a recognized element of the standard performance toolkit.

## Formula

```
SOAA = Accurate Commission Statements / Statements Issued
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_brokerage
- **Sector:** insurance_distribution

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1160 (batch 4)
