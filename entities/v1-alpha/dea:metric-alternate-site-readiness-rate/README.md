# dea:metric-alternate-site-readiness-rate

Candidate Performance Metric record for **Alternate Site Readiness Rate** (ASRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-alternate-site-readiness-rate`
- **Name:** Alternate Site Readiness Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ASRR

## 2. Definition

Alternate Site Readiness Rate (ASRR) measures exposure to adverse outcomes in the Business Continuity & Disaster Recovery domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Recovery Sites Passing Readiness Check / Recovery Sites, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether secondary sites and systems are provisioned, current, and ready to take load. Ready means tested at realistic load, not merely contracted. Sites restored to readiness only before audits are Potemkin. Read with disaster recovery test pass rate and workarea recovery capacity ratio.

## Formula

```
Recovery Sites Passing Readiness Check / Recovery Sites
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3522 (batch 8)
