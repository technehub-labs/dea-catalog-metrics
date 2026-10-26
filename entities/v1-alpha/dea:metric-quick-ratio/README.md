# dea:metric-quick-ratio

Candidate Performance Metric record for **Quick Ratio** (QR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-quick-ratio`
- **Name:** Quick Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** QR

## 2. Definition

Quick Ratio (QR) captures exposure to adverse outcomes for organizations tracking finance & accounting. It is defined as (Current Assets - Inventory) / Current Liabilities; the result is stated in ratio (x:1 or x). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the ability to cover current liabilities using only cash, marketable securities, and receivables, excluding inventory. It matters because inventory may not convert to cash quickly in a downturn, so this is the stricter test of immediate liquidity. Gaming risk lies in factoring or selling receivables just before period end to lift the numerator. Read with Working Capital Ratio and Days Sales Outstanding to judge receivables quality behind the ratio.

## Formula

```
(Current Assets - Inventory) / Current Liabilities
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 16 (batch 1)
