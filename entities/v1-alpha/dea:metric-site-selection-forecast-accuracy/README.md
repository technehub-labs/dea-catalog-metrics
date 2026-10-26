# dea:metric-site-selection-forecast-accuracy

Candidate Performance Metric record for **Site Selection Forecast Accuracy** (SSFA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-site-selection-forecast-accuracy`
- **Name:** Site Selection Forecast Accuracy
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SSFA

## 2. Definition

A Franchise & Multi-site indicator, Site Selection Forecast Accuracy (SSFA) quantifies the quality of outputs and outcomes. Its calculation is 1 - ABS(Actual Year-1 Sales - Forecast) / Forecast, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Franchise & multi-site practice.

## 3. Context

Site Selection Forecast Accuracy measures how closely pre-opening revenue forecasts match realized performance of new locations, and it is the compound-interest metric of multi-unit retail - every site decision locks in a decade of economics, so a forecasting model that is systematically off by 20 percent compounds into massive capital misallocation across dozens of locations. Measuring it requires discipline: compare against actuals at consistent milestones (year one, year two) and track bias separately from variance, since systematic optimism (forecast bias) is more fixable and more damaging than random error. Read with forecast error by market type and format, the analyst-versus-model attribution of misses, and post-mortem discipline on closed or underperforming locations.

## Formula

```
1 - ABS(Actual Year-1 Sales - Forecast) / Forecast
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** franchise_multi_site
- **Sector:** franchise_multi_site

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 812 (batch 2)
