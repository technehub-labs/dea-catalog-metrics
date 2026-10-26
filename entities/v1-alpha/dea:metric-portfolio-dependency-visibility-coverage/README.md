# dea:metric-portfolio-dependency-visibility-coverage

Candidate Performance Metric record for **Portfolio Dependency Visibility Coverage** (PDVC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-portfolio-dependency-visibility-coverage`
- **Name:** Portfolio Dependency Visibility Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PDVC

## 2. Definition

Within Program & Portfolio Management, Portfolio Dependency Visibility Coverage (PDVC) is used to gauge exposure to adverse outcomes. Its calculation is Initiatives with Mapped Dependencies / Initiatives, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of portfolio initiatives with mapped, monitored cross-initiative dependencies. Invisible dependencies turn independent delays into correlated portfolio failure. Coverage depends on honest declaration, which blame cultures discourage. Read with dependency closure timeliness and program interdependency health.

## Formula

```
Initiatives with Mapped Dependencies / Initiatives
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** program_portfolio_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2961 (batch 7)
