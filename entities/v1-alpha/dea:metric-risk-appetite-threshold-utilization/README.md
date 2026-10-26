# dea:metric-risk-appetite-threshold-utilization

Candidate Performance Metric record for **Risk Appetite Threshold Utilization** (RATU-GOV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-risk-appetite-threshold-utilization`
- **Name:** Risk Appetite Threshold Utilization
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RATU-GOV

## 2. Definition

Risk Appetite Threshold Utilization (RATU-GOV) captures exposure to adverse outcomes for organizations tracking enterprise decision effectiveness & governance monitoring. It is defined as Current Risk Position / Approved Appetite; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures how close actual risk positions run to approved appetite limits. Chronic utilization at or above 100% means the stated appetite is fictional. Thresholds defined too generously make utilization meaningless. Read with risk appetite statement effectiveness and portfolio risk concentration index.

## Formula

```
Current Risk Position / Approved Appetite
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** enterprise_decision_effectiveness_governance_monitoring

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3142 (batch 7)
