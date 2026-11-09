# dea:metric-collection-effectiveness-index

Candidate Performance Metric record for **Collection Effectiveness Index** (CEI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-collection-effectiveness-index`
- **Name:** Collection Effectiveness Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CEI

## 2. Definition

Within Professional Services, Collection Effectiveness Index (CEI) is used to gauge how efficiently resources are converted into outputs. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Collected Receivables / Receivables Due, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Professional services.

## 3. Context

Measures the share of receivables collected within terms over a period. It matters because it condenses the entire credit-to-cash cycle into one collection performance read. Teams can improve it by extending terms or writing off old debt, both of which flatter the numerator's difficulty. Read with Days Sales Outstanding and Write-Off Rate to confirm collection gains are real.

## Formula

```
CEI = Collected Receivables / Receivables Due
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** professional_services
- **Sector:** professional_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 681 (batch 2)
