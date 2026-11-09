# dea:metric-recovery-time-objective-compliance-rate

Candidate Performance Metric record for **Recovery Time Objective Compliance Rate** (RTOCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recovery-time-objective-compliance-rate`
- **Name:** Recovery Time Objective Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RTOCR

## 2. Definition

Within Business Continuity & Disaster Recovery, Recovery Time Objective Compliance Rate (RTOCR) is used to gauge exposure to adverse outcomes. It is computed as Services Restored within RTO in Tests / Services Tested, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether actual recovery capability meets declared RTOs when tested. Declared-but-unproven RTOs are the core fiction of continuity programs. Compliance assessed on paper rather than in tests overstates readiness. Read with disaster recovery test pass rate and maximum tolerable downtime headroom.

## Formula

```
RTOCR = Services Restored within RTO in Tests / Services Tested
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3517 (batch 8)
