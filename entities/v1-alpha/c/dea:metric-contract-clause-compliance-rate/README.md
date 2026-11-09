# dea:metric-contract-clause-compliance-rate

Candidate Performance Metric record for **Contract Clause Compliance Rate** (CCCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contract-clause-compliance-rate`
- **Name:** Contract Clause Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CCCR

## 2. Definition

Contract Clause Compliance Rate (CCCR) addresses conformance to standards, plans, or obligations and is a fixture of legal reporting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Contracts Containing All Required Clauses / Contracts Executed, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of executed contracts containing required standard clauses. It matters because missing clauses are latent legal and financial exposure discovered only at dispute time. Compliance can be inflated by waiving requirements informally without recording the exception. Read with Contract Renewal Leakage and Audit exception logs to confirm required clauses survive negotiation pressure.

## Formula

```
CCCR = Contracts Containing All Required Clauses / Contracts Executed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** legal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 389 (batch 1)
