# dea:metric-legacy-application-ratio

Candidate Performance Metric record for **Legacy Application Ratio** (LAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-legacy-application-ratio`
- **Name:** Legacy Application Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LAR

## 2. Definition

Legacy Application Ratio (LAR) measures exposure to adverse outcomes in the Enterprise Architecture domain. It is defined as Applications beyond Supported Platform / Total Applications; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of the application portfolio on unsupported, end-of-life, or obsolescent technology. It is a concise risk and agility indicator: high ratios predict slower change delivery, higher run cost, and security exposure. Definitional traps include whether extended-support vendor arrangements count as supported, and whether business-criticality weighting is applied. Read with technical debt remediation rate and legacy system migration progress.

## Formula

```
Applications beyond Supported Platform / Total Applications
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** enterprise_architecture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1350 (batch 5)
