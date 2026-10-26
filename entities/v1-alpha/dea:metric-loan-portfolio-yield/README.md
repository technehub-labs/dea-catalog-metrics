# dea:metric-loan-portfolio-yield

Candidate Performance Metric record for **Loan Portfolio Yield** (LPY) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-loan-portfolio-yield`
- **Name:** Loan Portfolio Yield
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LPY

## 2. Definition

Loan Portfolio Yield (LPY) captures the economic value created or preserved for organizations tracking banking & financial services. Its calculation is Loan Interest Income / Average Loan Portfolio, measured in percent (%). It originates from and is most used in Financial services practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Interest and fee income earned on the loan book as a percentage of average loans - the asset-side counterpart to funding cost in the NIM equation. It is where underwriting appetite becomes visible: a rising yield usually means reaching for riskier borrowers, longer tenors, or unsecured products, and the credit costs that follow arrive with a lag measured in years. The honest read is yield net of expected loss - a portfolio at 9 percent with 3 percent expected losses is worse than one at 6 percent with 40 basis points. Analysts decompose the movement between mix shift and repricing on a constant-currency, constant-mix basis before concluding that a bank has genuinely improved its asset mix.

## Formula

```
Loan Interest Income / Average Loan Portfolio
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 46 (batch 1)
