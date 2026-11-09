# dea:metric-shadow-vendor-discovery-rate

Candidate Performance Metric record for **Shadow Vendor Discovery Rate** (SVDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-shadow-vendor-discovery-rate`
- **Name:** Shadow Vendor Discovery Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SVDR

## 2. Definition

Shadow Vendor Discovery Rate (SVDR) measures exposure to adverse outcomes in the Third-Party Risk Management domain. It is defined as Unapproved Engagements Found per Review; the result is stated in count (items per period). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
SVDR = Unapproved Engagements Found per Review
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** third_party_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3729 (batch 8)
