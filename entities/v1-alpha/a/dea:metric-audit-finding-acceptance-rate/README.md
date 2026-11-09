# dea:metric-audit-finding-acceptance-rate

Candidate Performance Metric record for **Audit Finding Acceptance Rate** (AFAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-audit-finding-acceptance-rate`
- **Name:** Audit Finding Acceptance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AFAR

## 2. Definition

Audit Finding Acceptance Rate (AFAR) addresses the quality of outputs and outcomes and is a fixture of internal audit reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Findings Accepted by Management / Findings Raised, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of audit findings accepted by management without dispute. It matters because constant dispute signals either audit overreach or a culture of deflection. Acceptance can be gamed by accepting trivial findings while contesting material ones. Read with Management Action Closure Rate and repeat findings in future audits to confirm accepted findings get fixed, not just signed.

## Formula

```
AFAR = Findings Accepted by Management / Findings Raised
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_audit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 617 (batch 2)
