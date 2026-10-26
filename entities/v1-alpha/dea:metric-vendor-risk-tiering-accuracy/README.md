# dea:metric-vendor-risk-tiering-accuracy

Candidate Performance Metric record for **Vendor Risk Tiering Accuracy** (VRTA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vendor-risk-tiering-accuracy`
- **Name:** Vendor Risk Tiering Accuracy
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VRTA

## 2. Definition

Vendor Risk Tiering Accuracy (VRTA) captures the quality of outputs and outcomes for organizations tracking third-party risk management. It is computed as Tier Assignments Confirmed at Review / Tier Assignments, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Tier Assignments Confirmed at Review / Tier Assignments
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** third_party_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3732 (batch 8)
