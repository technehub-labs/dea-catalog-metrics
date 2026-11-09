# dea:metric-device-financing-portfolio-risk

Candidate Performance Metric record for **Device Financing Portfolio Risk** (DFPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-device-financing-portfolio-risk`
- **Name:** Device Financing Portfolio Risk
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DFPR

## 2. Definition

Within Telecom Product & Bundle Management, Device Financing Portfolio Risk (DFPR) is used to gauge exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Financing Balances Past Due / Total Financing Balances, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Telecommunications.

## 3. Context

Measures credit quality of the device installment and financing book - delinquency, default, and loss rates on financed handsets. As operators become consumer lenders, this separates real margin from receivables time bombs. Watch for vintage seasoning effects (early books look clean), underwriting loosening at launch seasons, and residual value assumptions on trade-in programs. Read with early payment default trends and provisioning coverage.

## Formula

```
DFPR = Financing Balances Past Due / Total Financing Balances
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecom_product_bundle_management
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1446 (batch 5)
