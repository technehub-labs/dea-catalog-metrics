# dea:metric-contract-renewal-leakage

Candidate Performance Metric record for **Contract Renewal Leakage** (CRL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contract-renewal-leakage`
- **Name:** Contract Renewal Leakage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CRL

## 2. Definition

Contract Renewal Leakage (CRL) measures exposure to adverse outcomes in the Legal domain. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Auto-Renewed Contracts without Review / Contracts Renewed, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures revenue or value lost at renewal through poor terms, missed auto-renewals, or un-negotiated uplift. It matters because renewal leakage is margin that already-earned relationships fail to capture. It can be understated by excluding contracts that lapsed entirely rather than renewed worse. Read with Contract Clause Compliance Rate and renewal term changes to see where value quietly drains.

## Formula

```
Auto-Renewed Contracts without Review / Contracts Renewed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** legal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 392 (batch 1)
