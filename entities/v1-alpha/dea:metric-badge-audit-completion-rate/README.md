# dea:metric-badge-audit-completion-rate

Candidate Performance Metric record for **Badge Audit Completion Rate** (BACR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-badge-audit-completion-rate`
- **Name:** Badge Audit Completion Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BACR

## 2. Definition

Within Physical Security Operations, Badge Audit Completion Rate (BACR) is used to gauge conformance to standards, plans, or obligations. It is computed as Access Reviews Completed / Reviews Scheduled, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of physical access badges audited within required cycles. It matters because stale badges are unauthorized access waiting to happen. Audits can be bulk-closed without actually reconciling access rights. Read with Access Anomaly findings and Separation events processing time to confirm audits remove stale access.

## Formula

```
Access Reviews Completed / Reviews Scheduled
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
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** physical_security_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1212 (batch 4)
