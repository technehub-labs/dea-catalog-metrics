# dea:metric-emergency-drill-compliance

Candidate Performance Metric record for **Emergency Drill Compliance** (EDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-emergency-drill-compliance`
- **Name:** Emergency Drill Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EDC

## 2. Definition

Emergency Drill Compliance (EDC) measures conformance to standards, plans, or obligations in the Physical Security Operations domain. The formula is Required Drills Completed on Schedule / Drills Required - reported in percent (%). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of required emergency drills completed on schedule. It matters because drill readiness is the only test of incident response that matters. Drills can degrade into scripted theater with known scenarios. Read with Drill Evaluation findings (time-to-objective) and unannounced drill results to confirm preparedness is real.

## Formula

```
Required Drills Completed on Schedule / Drills Required
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** physical_security_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1213 (batch 4)
