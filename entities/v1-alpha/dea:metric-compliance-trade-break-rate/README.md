# dea:metric-compliance-trade-break-rate

Candidate Performance Metric record for **Compliance Trade Break Rate** (CTBR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-compliance-trade-break-rate`
- **Name:** Compliance Trade Break Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CTBR

## 2. Definition

Compliance Trade Break Rate (CTBR) captures conformance to standards, plans, or obligations for organizations tracking investment management. It is computed as Trade Breaks Detected / Trades Executed, expressed in percent (%). Its use is concentrated in Asset management. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures failed compliance checks per executed trade. It matters because breaks are the raw signal of control weakness in regulated trading operations. Teams can reduce it by loosening pre-trade rule thresholds, trading control failure for throughput. Read with Regulatory Breach events and Exception Resolution Time to confirm fewer breaks mean stronger controls, not weaker tests.

## Formula

```
Trade Breaks Detected / Trades Executed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management
- **Sector:** asset_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 773 (batch 2)
