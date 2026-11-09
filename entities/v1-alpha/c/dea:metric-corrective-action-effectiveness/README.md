# dea:metric-corrective-action-effectiveness

Candidate Performance Metric record for **Corrective Action Effectiveness** (CAE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-corrective-action-effectiveness`
- **Name:** Corrective Action Effectiveness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CAE

## 2. Definition

Within Quality Management, Corrective Action Effectiveness (CAE) is used to gauge the quality of outputs and outcomes. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Actions Verified Effective / Actions Implemented, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether corrective actions actually prevented recurrence of the original problem. It matters because the point of CAPA is permanence, not filing. It can be gamed by declaring success before enough exposure time has elapsed for recurrence. Read with Problem Recurrence Rate and Audit Nonconformance Closure Rate to confirm effectiveness claims survive real-world time.

## Formula

```
CAE = Actions Verified Effective / Actions Implemented
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 239 (batch 1)
