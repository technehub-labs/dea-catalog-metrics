# dea:metric-recovery-time-objective-attainment

Candidate Performance Metric record for **Recovery Time Objective Attainment** (RTOA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recovery-time-objective-attainment`
- **Name:** Recovery Time Objective Attainment
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RTOA

## 2. Definition

Recovery Time Objective Attainment (RTOA) addresses exposure to adverse outcomes and is a fixture of business resilience & continuity reporting. It is computed as Recoveries within RTO in Tests or Events / Recovery Tests, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether critical services were restored within their target recovery time in actual incidents or tests. RTOs are promises; attainment shows whether resilience spending matches operational reality. Be strict about the clock: attainment measured from incident declaration rather than disruption start flatters performance, and untested RTOs are hopes, not capabilities. Read with disaster recovery test frequency compliance and resilience stress test pass rate.

## Formula

```
Recoveries within RTO in Tests or Events / Recovery Tests
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1408 (batch 5)
