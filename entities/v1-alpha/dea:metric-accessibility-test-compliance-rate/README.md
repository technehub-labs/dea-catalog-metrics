# dea:metric-accessibility-test-compliance-rate

Candidate Performance Metric record for **Accessibility Test Compliance Rate** (ATCR-QA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-accessibility-test-compliance-rate`
- **Name:** Accessibility Test Compliance Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ATCR-QA

## 2. Definition

Accessibility Test Compliance Rate (ATCR-QA) measures conformance to standards, plans, or obligations in the Software Testing & Quality Engineering domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is WCAG Checks Passed / Checks, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of interfaces and user flows passing WCAG-based automated and manual accessibility checks. Accessibility is both a legal exposure and a market-inclusion play, and retrofitting is far costlier than building it in. Automated tools catch only a minority of barriers, so a clean score can overstate true conformance. Read with accessibility compliance rate and UX research coverage.

## Formula

```
WCAG Checks Passed / Checks
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** software_testing_quality_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2725 (batch 7)
