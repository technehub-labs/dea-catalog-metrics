# dea:metric-collateral-dispute-rate

Candidate Performance Metric record for **Collateral Dispute Rate** (CDR-IR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-collateral-dispute-rate`
- **Name:** Collateral Dispute Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDR-IR

## 2. Definition

Collateral Dispute Rate (CDR-IR) measures the quality of outputs and outcomes in the Investment Risk & Middle Office Operations domain. Its calculation is Collateral Disputes / Collateral Calls, measured in percent (%). It originates from and is most used in Investment management practice. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
CDR-IR = Collateral Disputes / Collateral Calls
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_risk_middle_office_operations
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3468 (batch 7)
