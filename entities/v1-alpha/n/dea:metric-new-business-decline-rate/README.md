# dea:metric-new-business-decline-rate

Candidate Performance Metric record for **New Business Decline Rate** (NBDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-new-business-decline-rate`
- **Name:** New Business Decline Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NBDR

## 2. Definition

Within Insurance Underwriting, New Business Decline Rate (NBDR) is used to gauge exposure to adverse outcomes. It is computed as Risks Declined / Risks Submitted, expressed in percent (%). Its use is concentrated in Insurance. It is reviewed at cadence by planning owners to correct course before issues become strategic. Values outside the intended band, on either side, warrant investigation.

## Formula

```
NBDR = Risks Declined / Risks Submitted
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1504 (batch 6)
