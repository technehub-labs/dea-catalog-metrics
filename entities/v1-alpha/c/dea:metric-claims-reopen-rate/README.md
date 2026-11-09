# dea:metric-claims-reopen-rate

Candidate Performance Metric record for **Claims Reopen Rate** (CRR-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-claims-reopen-rate`
- **Name:** Claims Reopen Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRR-C

## 2. Definition

Claims Reopen Rate (CRR-C) captures the quality of outputs and outcomes for organizations tracking claims operations (insurance). It is computed as Reopened Claims / Claims Closed, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is concentrated in Insurance.

## 3. Context

Measures the share of closed claims later reopened. It matters because reopenings expose premature closures and rework cost. Adjusters can avoid reopening by paying marginally to keep claims closed, trading accuracy for metric health. Read with Claim Estimate Accuracy and Complaint trends to confirm closure quality.

## Formula

```
CRR-C = Reopened Claims / Claims Closed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** claims_operations_insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 850 (batch 3)
