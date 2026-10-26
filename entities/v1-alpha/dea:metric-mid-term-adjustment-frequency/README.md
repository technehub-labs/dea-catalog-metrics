# dea:metric-mid-term-adjustment-frequency

Candidate Performance Metric record for **Mid-Term Adjustment Frequency** (MTAF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mid-term-adjustment-frequency`
- **Name:** Mid-Term Adjustment Frequency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MTAF

## 2. Definition

Mid-Term Adjustment Frequency (MTAF) addresses exposure to adverse outcomes and is a fixture of insurance underwriting reporting. It is defined as Mid-Term Adjustments / Active Policies; the result is stated in times per period. In Insurance, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. Values outside the intended band, on either side, warrant investigation.

## Formula

```
MTAF = Mid-Term Adjustments / Active Policies
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1522 (batch 6)
