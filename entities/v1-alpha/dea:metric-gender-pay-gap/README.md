# dea:metric-gender-pay-gap

Candidate Performance Metric record for **Gender Pay Gap** (GPG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gender-pay-gap`
- **Name:** Gender Pay Gap
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** GPG

## 2. Definition

A Human Resources indicator, Gender Pay Gap (GPG) quantifies conformance to standards, plans, or obligations. The formula is (Median Male Pay - Median Female Pay) / Median Male Pay - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The difference between average male and female pay, expressed as a percentage - not of equal work, which is the equal-pay question, but of the whole organization, which makes it a structure metric rather than only a fairness one. That distinction is its strategic content: a gap can persist with perfectly equal pay for identical roles because men are overrepresented in higher-paid jobs, so closing it requires changing who gets promoted into which roles, not adjusting salaries. jurisdictions from the UK to the EU now mandate public disclosure, which has turned the metric into an employer-brand and investor-relations number as much as a compliance one. Quartile-level reporting, which the disclosure regimes increasingly require, is where the diagnosis actually lives.

## Formula

```
(Median Male Pay - Median Female Pay) / Median Male Pay
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 146 (batch 1)
