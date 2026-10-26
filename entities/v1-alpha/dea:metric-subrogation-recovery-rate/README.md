# dea:metric-subrogation-recovery-rate

Candidate Performance Metric record for **Subrogation Recovery Rate** (SRR-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-subrogation-recovery-rate`
- **Name:** Subrogation Recovery Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SRR-C

## 2. Definition

A Claims Operations (Insurance) indicator, Subrogation Recovery Rate (SRR-C) quantifies the economic value created or preserved. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Recovered Amounts from Third Parties / Recoverable Amounts, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Insurance.

## 3. Context

Measures the share of claim losses recovered from responsible third parties. It matters because subrogation is pure recovered loss that directly improves combined ratio. Recovery can be suppressed by quick settlements that waive subrogation rights. Read with Claims Cost per File Handled and recovery cycle time to confirm recoveries are pursued, not traded.

## Formula

```
Recovered Amounts from Third Parties / Recoverable Amounts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** claims_operations_insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 853 (batch 3)
