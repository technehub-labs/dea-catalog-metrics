# dea:metric-claim-estimate-accuracy

Candidate Performance Metric record for **Claim Estimate Accuracy** (CEA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-claim-estimate-accuracy`
- **Name:** Claim Estimate Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CEA

## 2. Definition

A Claims Operations (Insurance) indicator, Claim Estimate Accuracy (CEA) quantifies the quality of outputs and outcomes. Its calculation is 1 - ABS(Initial Reserve - Final Settlement) / Final Settlement, measured in percent (%). It originates from and is most used in Insurance practice. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how closely initial claim estimates match ultimate settlement cost. It matters because reserving errors distort both customer experience and financial statements. Gaming risk includes releasing reserves early to book underwriting gains. Read with Claims Reopen Rate and Reserve Development to confirm accuracy is genuine.

## Formula

```
CEA = 1 - ABS(Initial Reserve - Final Settlement) / Final Settlement
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** claims_operations_insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 852 (batch 3)
