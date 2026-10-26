# dea:metric-application-portfolio-rationalization

Candidate Performance Metric record for **Application Portfolio Rationalization** (APR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-application-portfolio-rationalization`
- **Name:** Application Portfolio Rationalization
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** APR

## 2. Definition

A Enterprise Architecture indicator, Application Portfolio Rationalization (APR) quantifies how efficiently resources are converted into outputs. It is computed as Applications Retired or Consolidated / Applications Identified, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures progress in shrinking the application estate - retirements, consolidations, platform migrations against plan. Bloated portfolios multiply integration cost, security surface, and change friction, so rationalization is one of the few IT moves that pays twice. Be skeptical of counts alone: retiring ten small apps while adding one giant incapable platform can be regression. Read with application overlap index and legacy cost run-rate reduction.

## Formula

```
Applications Retired or Consolidated / Applications Identified
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** enterprise_architecture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1344 (batch 5)
