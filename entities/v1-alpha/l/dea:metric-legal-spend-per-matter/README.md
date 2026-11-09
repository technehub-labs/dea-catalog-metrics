# dea:metric-legal-spend-per-matter

Candidate Performance Metric record for **Legal Spend per Matter** (LSPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-legal-spend-per-matter`
- **Name:** Legal Spend per Matter
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LSPM

## 2. Definition

Within Legal, Legal Spend per Matter (LSPM) is used to gauge how efficiently resources are converted into outputs. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Total Legal Cost / Matters Handled, measured in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures average legal cost per matter or case. It matters because it benchmarks outside counsel efficiency and reveals matter scoping problems. Gaming risk includes splitting matters to shrink the average or capitalizing spend outside the legal budget. Read with Contract Cycle Time and matter outcome data to weigh cost against results rather than in isolation.

## Formula

```
LSPM = Total Legal Cost / Matters Handled
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
- **Domain:** legal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 391 (batch 1)
