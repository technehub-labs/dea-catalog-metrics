# dea:metric-return-on-capital-employed

Candidate Performance Metric record for **Return on Capital Employed** (ROCE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-return-on-capital-employed`
- **Name:** Return on Capital Employed
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ROCE

## 2. Definition

Return on Capital Employed (ROCE) captures the economic value created or preserved for organizations tracking finance & accounting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as EBIT / (Total Assets - Current Liabilities), expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

EBIT over capital employed (total assets minus current liabilities) - the pre-tax, pre-financing cousin of ROIC. It is the standard profitability lens in capital-intensive industries and in UK practice, where it long predates the ROIC fashion. The numerator deliberately excludes interest so the measure is independent of funding mix, making it a clean gauge of operational asset productivity; the denominator captures the long-term money committed to operations. Like all return-on-capital measures it punishes balance sheets that carry idle assets, so a falling ROCE often precedes restructuring announcements. It pairs naturally with the spread over borrowing cost: a ROCE persistently below the interest rate means growth is being financed at a loss.

## Formula

```
EBIT / (Total Assets - Current Liabilities)
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
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 14 (batch 1)
