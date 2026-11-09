# dea:metric-recovery-point-objective-attainment

Candidate Performance Metric record for **Recovery Point Objective Attainment** (RPOA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recovery-point-objective-attainment`
- **Name:** Recovery Point Objective Attainment
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RPOA

## 2. Definition

Recovery Point Objective Attainment (RPOA) addresses exposure to adverse outcomes and is a fixture of business resilience & continuity reporting. Its calculation is Recoveries within RPO / Recovery Validations, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether data loss in actual incidents stayed within the tolerable recovery point - the maximum data a process can afford to lose. It is the data-loss twin of RTO: a service can come back fast but with unusable, stale data. Honest measurement requires verification of restored data integrity, not just system availability. Read with backup verification coverage and recovery time objective attainment.

## Formula

```
RPOA = Recoveries within RPO / Recovery Validations
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_resilience_continuity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1409 (batch 5)
