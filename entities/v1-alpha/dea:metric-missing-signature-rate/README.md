# dea:metric-missing-signature-rate

Candidate Performance Metric record for **Missing Signature Rate** (MSR-CL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-missing-signature-rate`
- **Name:** Missing Signature Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MSR-CL

## 2. Definition

Missing Signature Rate (MSR-CL) addresses exposure to adverse outcomes and is a fixture of contract lifecycle management reporting. It is computed as Counterparty-Unsigned Contracts in Force / Contracts Sampled, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Counterparty-Unsigned Contracts in Force / Contracts Sampled
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contract_lifecycle_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3705 (batch 8)
