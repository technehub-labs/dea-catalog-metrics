# dea:metric-working-capital-ratio-deep-dive

Candidate Performance Metric record for **Working Capital Ratio (Deep Dive)** (WCR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-working-capital-ratio-deep-dive`
- **Name:** Working Capital Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WCR-D

## 2. Definition

Working Capital Ratio (Deep Dive) (WCR-D) addresses exposure to adverse outcomes and is a fixture of corporate treasury (deep dive) reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Current Assets / Current Liabilities, measured in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures current assets against current liabilities, the classic short-term solvency gauge. Beyond balance-sheet optics, it is the efficiency dial of the cash engine: excess working capital is capital with negative carry, and deficits are refinancing risk. Ratio movements need decomposition, since a ratio rising from slowing receivables is deterioration dressed as safety. Read with cash conversion cycle (Deep Dive) and peer-benchmark context.

## Formula

```
WCR-D = Current Assets / Current Liabilities
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_treasury_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2181 (batch 6)
