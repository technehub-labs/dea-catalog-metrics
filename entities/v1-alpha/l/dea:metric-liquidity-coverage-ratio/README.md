# dea:metric-liquidity-coverage-ratio

Candidate Performance Metric record for **Liquidity Coverage Ratio** (LCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-liquidity-coverage-ratio`
- **Name:** Liquidity Coverage Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LCR

## 2. Definition

Liquidity Coverage Ratio (LCR) measures exposure to adverse outcomes in the Banking & Financial Services domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is High-Quality Liquid Assets / Net Cash Outflows over 30 Days, measured in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Financial services practice.

## 3. Context

The stock of high-quality liquid assets divided by net cash outflows over a 30-day stress - Basel III's answer to the discovery that banks failed in 2008 not from insolvency but from funding evaporating in weeks. It forces each bank to hold assets it can sell even when markets close, sized to a standardized stress scenario of deposit runs and wholesale withdrawal. The design choices matter: the 30-day window matches the time regulators need to resolve a bank, and the outflow assumptions are prescribed per funding type, which quietly penalizes flighty wholesale funding relative to sticky retail deposits. A compliant ratio is a floor, not a strategy - firms manage well above it because the metric is point-in-time and the stress it assumes is a scenario, not a ceiling.

## Formula

```
LCR = High-Quality Liquid Assets / Net Cash Outflows over 30 Days
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 41 (batch 1)
