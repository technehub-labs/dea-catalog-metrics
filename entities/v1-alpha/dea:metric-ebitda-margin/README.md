# dea:metric-ebitda-margin

Candidate Performance Metric record for **EBITDA Margin** (EBITDA%) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ebitda-margin`
- **Name:** EBITDA Margin
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EBITDA%

## 2. Definition

Within Finance & Accounting, EBITDA Margin (EBITDA%) is used to gauge the economic value created or preserved. Its calculation is EBITDA / Revenue, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

EBITDA margin takes earnings before interest, tax, depreciation, and amortization over revenue, approximating the cash the operating business generates before capital structure and non-cash accounting charges. It became the universal currency of valuation because it neutralizes differences in leverage, tax regime, and depreciation schedules that would otherwise distort comparisons between firms. Its blind spot is exactly what it removes: capital intensity. Two companies with identical EBITDA margins can have entirely different economics if one must reinvest most of its EBITDA in plant while the other leases everything. Use it as a starting point for enterprise-value multiples, never as a proxy for cash flow on its own.

## Formula

```
EBITDA / Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 10 (batch 1)
