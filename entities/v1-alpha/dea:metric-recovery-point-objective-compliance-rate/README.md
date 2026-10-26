# dea:metric-recovery-point-objective-compliance-rate

Candidate Performance Metric record for **Recovery Point Objective Compliance Rate** (RPOCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recovery-point-objective-compliance-rate`
- **Name:** Recovery Point Objective Compliance Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RPOCR

## 2. Definition

Within Business Continuity & Disaster Recovery, Recovery Point Objective Compliance Rate (RPOCR) is used to gauge exposure to adverse outcomes. The formula is Data Restored within RPO in Tests / Data Restores Tested - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether achievable data loss windows meet declared RPOs. RPO failures mean silent data loss, which no speed of recovery can repair. RPOs verified only for backups but not replication paths are half-proven. Read with backup restore success rate and recovery time objective compliance rate.

## Formula

```
Data Restored within RPO in Tests / Data Restores Tested
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_continuity_disaster_recovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3518 (batch 8)
