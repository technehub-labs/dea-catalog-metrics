# dea:metric-critical-application-recovery-sequence-coverage

Candidate Performance Metric record for **Critical Application Recovery Sequence Coverage** (CARSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-critical-application-recovery-sequence-coverage`
- **Name:** Critical Application Recovery Sequence Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CARSC

## 2. Definition

Critical Application Recovery Sequence Coverage (CARSC) captures conformance to standards, plans, or obligations for organizations tracking business continuity & disaster recovery. It provides the day-to-day signal that a process is running as designed. Its calculation is Applications in Documented Runbook Sequence / Critical Applications, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
CARSC = Applications in Documented Runbook Sequence / Critical Applications
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_continuity_disaster_recovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3525 (batch 8)
