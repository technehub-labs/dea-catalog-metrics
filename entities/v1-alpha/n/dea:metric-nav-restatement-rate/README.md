# dea:metric-nav-restatement-rate

Candidate Performance Metric record for **NAV Restatement Rate** (NAVRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-nav-restatement-rate`
- **Name:** NAV Restatement Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NAVRR

## 2. Definition

A Investment Risk & Middle Office Operations indicator, NAV Restatement Rate (NAVRR) quantifies the quality of outputs and outcomes. Its calculation is NAVs Restated / NAVs Published, measured in events per thousand or million (scaled). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Investment management practice.

## Formula

```
NAVRR = NAVs Restated / NAVs Published
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3462 (batch 7)
