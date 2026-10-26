# dea:metric-defect-density

Candidate Performance Metric record for **Defect Density** (DD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-defect-density`
- **Name:** Defect Density
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DD

## 2. Definition

Defect Density (DD) measures the quality of outputs and outcomes in the Software Engineering domain. Its calculation is Defects per 1,000 Lines of Code or Function Point, measured in ratio (x:1 or x). Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures defects per unit of size, usually per thousand lines of code or per story. It matters because it normalizes quality comparison across components and releases. It can be gamed by discouraging defect logging or splitting code to inflate the denominator. Read with Defect Escape Rate and Code Review findings to check density reflects true quality, not reporting culture.

## Formula

```
Defects per 1,000 Lines of Code or Function Point
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 294 (batch 1)
