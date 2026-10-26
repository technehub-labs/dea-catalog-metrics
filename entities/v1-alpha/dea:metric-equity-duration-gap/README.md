# dea:metric-equity-duration-gap

Candidate Performance Metric record for **Equity Duration Gap** (EDG-VCF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-equity-duration-gap`
- **Name:** Equity Duration Gap
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EDG-VCF

## 2. Definition

Equity Duration Gap (EDG-VCF) captures exposure to adverse outcomes for organizations tracking valuation & corporate finance standard measures. Its calculation is Duration of Assets minus Duration of Liabilities, measured in ratio (x:1 or x). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures the mismatch in sensitivity between asset and equity values to rate or growth shifts. The gap quantifies how exposed shareholder value is to duration-affecting shocks. Gap models calibrated on calm regimes fail in repricing events. Read with interest rate risk in the banking book and stress test scenario coverage.

## Formula

```
Duration of Assets minus Duration of Liabilities
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** valuation_corporate_finance_standard_measures

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4053 (batch 9)
