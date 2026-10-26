# dea:metric-building-operating-cost-escalation

Candidate Performance Metric record for **Building Operating Cost Escalation** (BOCE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-building-operating-cost-escalation`
- **Name:** Building Operating Cost Escalation
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BOCE

## 2. Definition

Within Facilities & Real Estate, Building Operating Cost Escalation (BOCE) is used to gauge how efficiently resources are converted into outputs. Its calculation is (Cost_current - Cost_prior) / Cost_prior, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures year-over-year growth in building operating expenses. It matters because lease economics and portfolio ROI erode quietly when escalation outruns rent uplift. Escalation can be masked by deferring capital repairs into future budget years. Read with Energy Intensity and Facility Condition Index to confirm cost restraint is efficiency, not deferred maintenance debt.

## Formula

```
(Cost_current - Cost_prior) / Cost_prior
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facilities_real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 458 (batch 1)
