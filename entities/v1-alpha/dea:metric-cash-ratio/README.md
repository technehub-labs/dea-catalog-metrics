# dea:metric-cash-ratio

Candidate Performance Metric record for **Cash Ratio** (CR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cash-ratio`
- **Name:** Cash Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CR

## 2. Definition

Cash Ratio (CR) captures exposure to adverse outcomes for organizations tracking finance & accounting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as (Cash + Cash Equivalents) / Current Liabilities, expressed in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of current liabilities covered by cash and cash equivalents alone. It is the most conservative liquidity test and matters in industries with volatile cash flows or tight credit access. A high value may simply reflect hoarding that drags return on assets, and managers can park short-term borrowings as cash to window-dress it. Read with Working Capital Ratio and Interest Coverage Ratio to distinguish prudence from inefficient capital deployment.

## Formula

```
(Cash + Cash Equivalents) / Current Liabilities
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 17 (batch 1)
