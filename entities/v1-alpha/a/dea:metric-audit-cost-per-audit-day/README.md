# dea:metric-audit-cost-per-audit-day

Candidate Performance Metric record for **Audit Cost per Audit Day** (ACPAD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-audit-cost-per-audit-day`
- **Name:** Audit Cost per Audit Day
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ACPAD

## 2. Definition

Audit Cost per Audit Day (ACPAD) measures how efficiently resources are converted into outputs in the Internal Audit domain. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Internal Audit Cost / Audit Days Performed, expressed in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures average cost of one audit engagement day. It matters because it benchmarks internal audit efficiency against external providers. Gaming risk includes squeezing scope per day or relying on cheaper, less experienced staff that lowers quality. Read with Stakeholder Satisfaction with Audit and coverage plan completion to confirm efficiency is not bought with audit depth.

## Formula

```
ACPAD = Internal Audit Cost / Audit Days Performed
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_audit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 618 (batch 2)
