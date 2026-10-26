# dea:metric-return-on-assets

Candidate Performance Metric record for **Return on Assets** (ROA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-return-on-assets`
- **Name:** Return on Assets
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ROA

## 2. Definition

Return on Assets (ROA) addresses the economic value created or preserved and is a fixture of finance & accounting reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Net Income / Total Assets; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Net income divided by total assets - the classic test of how hard the balance sheet is working. The DuPont identity showed a century ago that this single number decomposes into margin times asset turnover, which is its real strategic power: a retailer earns ROA through velocity and a utility through margin, and the decomposition tells you which lever each business actually pulls. Because the denominator mixes productive and non-productive assets, a rising ROA can reflect asset disposals as easily as better trading. Comparisons are only meaningful within industries with similar asset intensity, and the average-asset convention smooths the seasonal distortion of year-end snapshots.

## Formula

```
Net Income / Total Assets
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 11 (batch 1)
