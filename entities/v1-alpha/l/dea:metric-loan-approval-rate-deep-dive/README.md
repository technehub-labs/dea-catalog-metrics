# dea:metric-loan-approval-rate-deep-dive

Candidate Performance Metric record for **Loan Approval Rate (Deep Dive)** (LAR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-loan-approval-rate-deep-dive`
- **Name:** Loan Approval Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LAR-D

## 2. Definition

Loan Approval Rate (Deep Dive) (LAR-D) addresses growth over time and is a fixture of banking retail lending (deep dive) reporting. It is computed as Approved Applications / Applications, expressed in percent (%). Its use is concentrated in Banking. It is reviewed at cadence by planning owners to correct course before issues become strategic. Values outside the intended band, on either side, warrant investigation.

## Formula

```
LAR-D = Approved Applications / Applications
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** banking_retail_lending_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2074 (batch 6)
