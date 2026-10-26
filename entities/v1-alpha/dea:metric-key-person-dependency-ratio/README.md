# dea:metric-key-person-dependency-ratio

Candidate Performance Metric record for **Key-Person Dependency Ratio** (KPDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-key-person-dependency-ratio`
- **Name:** Key-Person Dependency Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** KPDR

## 2. Definition

Within Business Resilience & Continuity, Key-Person Dependency Ratio (KPDR) is used to gauge exposure to adverse outcomes. The formula is Critical Roles without Deputies / Critical Roles - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of critical processes, systems, or relationships that depend on individuals without adequate backup or documentation. It quantifies a risk every manager intuitively knows and rarely manages, and it predicts both outage duration and succession fragility. Honest measurement requires criticality weighting - all dependencies are not equal - and refreshing the dependency map after every reorg. Read with critical knowledge retention risk and successor readiness ratio.

## Formula

```
Critical Roles without Deputies / Critical Roles
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_resilience_continuity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1416 (batch 5)
