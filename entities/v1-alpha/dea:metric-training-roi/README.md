# dea:metric-training-roi

Candidate Performance Metric record for **Training ROI** (TRoi) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-training-roi`
- **Name:** Training ROI
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TRoi

## 2. Definition

Within Human Resources, Training ROI (TRoi) is used to gauge the economic value created or preserved. It is computed as (Productivity Gain - Training Cost) / Training Cost, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the business return generated per unit of training investment. It matters because it shifts L&D from a cost center to a value-justified function. Estimates are easy to game by attributing broad productivity gains to a single program. Read with Time to Productivity and Internal Fill Rate to tie training claims to observable capability outcomes.

## Formula

```
(Productivity Gain - Training Cost) / Training Cost
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 140 (batch 1)
