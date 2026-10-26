# dea:metric-budget-overrun-rate

Candidate Performance Metric record for **Budget Overrun Rate** (BOR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-budget-overrun-rate`
- **Name:** Budget Overrun Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BOR

## 2. Definition

Budget Overrun Rate (BOR) addresses exposure to adverse outcomes and is a fixture of project management reporting. It is defined as Projects Exceeding Budget / Projects Completed; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The degree to which actual project cost exceeds the approved budget - expressed as a percentage of overrun or as the share of projects exceeding budget. Its strategic significance is the estimating-culture signal it carries: chronic overruns against original budgets indicate that budgets are set as aspiration rather than forecast, which corrupts the entire capital-allocation process, since projects compete for funds on numbers no one believes. The reference-class forecasting tradition (Flyvbjerg's work on megaprojects) argues that overruns are so systematic that the outside view - the distribution of outcomes from similar past projects - predicts cost better than any inside estimate, and this metric is the input that makes outside-view forecasting possible. Read overrun against scope change: cost per unit of delivered scope is the honest comparator when scope legitimately moved.

## Formula

```
Projects Exceeding Budget / Projects Completed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 358 (batch 1)
