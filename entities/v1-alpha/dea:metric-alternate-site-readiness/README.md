# dea:metric-alternate-site-readiness

Candidate Performance Metric record for **Alternate Site Readiness** (ASR-B) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-alternate-site-readiness`
- **Name:** Alternate Site Readiness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ASR-B

## 2. Definition

Alternate Site Readiness (ASR-B) measures conformance to standards, plans, or obligations in the Business Resilience & Continuity domain. The formula is Alternate Sites Ready and Tested / Required Alternate Sites - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of critical operations with tested, ready alternate sites for continuity. It matters because untested continuity plans fail exactly when needed. Readiness can be declared on paper without a full failover test. Read with Failover Test Results and Recovery Time achieved in drills to confirm readiness is operational.

## Formula

```
ASR-B = Alternate Sites Ready and Tested / Required Alternate Sites
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_resilience_continuity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1417 (batch 5)
