# dea:metric-fraud-detection-rate

Candidate Performance Metric record for **Fraud Detection Rate** (FDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fraud-detection-rate`
- **Name:** Fraud Detection Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FDR

## 2. Definition

A Insurance indicator, Fraud Detection Rate (FDR) quantifies exposure to adverse outcomes. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Fraudulent Claims Detected / Total Fraudulent Claims Estimated - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Insurance sector.

## 3. Context

Measures the share of fraud attempts or fraud losses that detection systems successfully catch. It matters because undetected fraud erodes claims and underwriting economics and regulatory standing. A rising rate can be gamed by tightening thresholds until legitimate claims start being flagged, harming honest customers. Read with False Positive Rate in fraud screening and Claims Leakage to balance detection aggressiveness against customer harm.

## Formula

```
FDR = Fraudulent Claims Detected / Total Fraudulent Claims Estimated
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 65 (batch 1)
