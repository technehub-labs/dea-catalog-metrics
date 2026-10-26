# dea:metric-business-impact-analysis-currency

Candidate Performance Metric record for **Business Impact Analysis Currency** (BIAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-business-impact-analysis-currency`
- **Name:** Business Impact Analysis Currency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BIAC

## 2. Definition

Business Impact Analysis Currency (BIAC) captures conformance to standards, plans, or obligations for organizations tracking business continuity & disaster recovery. The formula is BIAs Refreshed within Cycle / Critical Processes - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether BIAs are recent enough to reflect current processes, systems, and dependencies. A stale BIA misallocates recovery priorities to yesterday's business. Currency without quality (impact scoring rigor) is date hygiene. Read with business continuity plan coverage (Deep Dive) and recovery time objective compliance rate.

## Formula

```
BIAs Refreshed within Cycle / Critical Processes
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3516 (batch 8)
