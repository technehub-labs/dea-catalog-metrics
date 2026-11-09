# dea:metric-working-capital-ratio

Candidate Performance Metric record for **Working Capital Ratio** (WCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-working-capital-ratio`
- **Name:** Working Capital Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WCR

## 2. Definition

Working Capital Ratio (WCR) addresses exposure to adverse outcomes and is a fixture of finance & accounting reporting. It is defined as Current Assets / Current Liabilities; the result is stated in ratio (x:1 or x). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures the ratio of current assets to current liabilities, showing how comfortably a firm can cover near-term obligations. It is a core read on operating liquidity and short-term financial resilience for creditors and managers alike. An excessively high ratio can signal idle cash or bloated inventory rather than strength, while window-dressing via payables timing at period close can inflate it. Read with Cash Conversion Cycle and Days Payable Outstanding to separate genuine liquidity from balance-sheet timing.

## Formula

```
WCR = Current Assets / Current Liabilities
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 15 (batch 1)
