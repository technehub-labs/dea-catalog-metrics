# dea:metric-debt-to-equity-ratio

Candidate Performance Metric record for **Debt-to-Equity Ratio** (D/E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-debt-to-equity-ratio`
- **Name:** Debt-to-Equity Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** D/E

## 2. Definition

Debt-to-Equity Ratio (D/E) measures exposure to adverse outcomes in the Finance & Accounting domain. It is defined as Total Debt / Shareholders' Equity; the result is stated in ratio (x:1 or x). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Total debt over shareholders equity - the oldest leverage gauge in corporate finance. It frames the capital structure as a balance between other people's money and the owners', which is why lenders treat it as a covenant anchor and rating agencies as a threshold input. The number that counts as prudent swings wildly by sector: below 0.5 in cyclical manufacturing is comfortable, while 2.0 can be normal for a regulated utility with contracted cash flows. Its blind spots are disguised debt (leases, guarantees, payables stretching) and book equity distorted by buybacks and accumulated profits. Read it with interest coverage: the same ratio can be safe or reckless depending on the cash available to service it.

## Formula

```
D/E = Total Debt / Shareholders' Equity
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
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 18 (batch 1)
