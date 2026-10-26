# dea:metric-denial-overturn-rate

Candidate Performance Metric record for **Denial Overturn Rate** (DOR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-denial-overturn-rate`
- **Name:** Denial Overturn Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DOR

## 2. Definition

Denial Overturn Rate (DOR) addresses how effectively a process or entity achieves its intended outcome and is a fixture of healthcare revenue cycle reporting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Denials Reversed on Appeal / Denials Appealed, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Healthcare.

## 3. Context

Measures the share of denied claims successfully appealed and paid. It matters because it captures recoverable revenue lost to process failure and persistence. Teams can inflate it by appealing only easy denials while writing off complex ones. Read with Claim Denial Rate and Write-Off Rate to confirm appeal effort targets material revenue.

## Formula

```
Denials Reversed on Appeal / Denials Appealed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** healthcare_revenue_cycle
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 874 (batch 3)
