# dea:metric-peg-ratio

Candidate Performance Metric record for **PEG Ratio** (PEGR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-peg-ratio`
- **Name:** PEG Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PEGR

## 2. Definition

PEG Ratio (PEGR) measures the economic value created or preserved in the Valuation & Corporate Finance Standard Measures domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Price-to-Earnings / Expected Earnings Growth, measured in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the price-to-earnings multiple relative to earnings growth rate. It prices growth honestly: a high multiple is fine if growth is real. Growth estimates in the denominator are hope with decimals. Read with earnings yield (Deep Dive) and compound annual growth rate (Deep Dive).

## Formula

```
PEGR = Price-to-Earnings / Expected Earnings Growth
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4045 (batch 9)
