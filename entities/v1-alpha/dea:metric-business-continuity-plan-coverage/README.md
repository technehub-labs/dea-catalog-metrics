# dea:metric-business-continuity-plan-coverage

Candidate Performance Metric record for **Business Continuity Plan Coverage** (BCPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-business-continuity-plan-coverage`
- **Name:** Business Continuity Plan Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BCPC

## 2. Definition

Business Continuity Plan Coverage (BCPC) measures conformance to standards, plans, or obligations in the Business Resilience & Continuity domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Critical Processes with Current Tested BCP / Critical Processes - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of critical business processes with current, exercised continuity plans. Coverage gaps are the geometric predictor of extended outages: the unplanned-for process is where incident response improvises. Currency matters more than existence - a plan untouched since the last reorganization is negative coverage. Read with disaster recovery test frequency compliance and key-person dependency ratio.

## Formula

```
Critical Processes with Current Tested BCP / Critical Processes
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1410 (batch 5)
