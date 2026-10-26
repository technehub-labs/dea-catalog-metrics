# dea:metric-seasonal-occupancy-variance

Candidate Performance Metric record for **Seasonal Occupancy Variance** (SOV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-seasonal-occupancy-variance`
- **Name:** Seasonal Occupancy Variance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SOV

## 2. Definition

Within Travel & Tourism, Seasonal Occupancy Variance (SOV) is used to gauge the utilization or availability of capacity. It is computed as (Peak Occupancy - Off-Peak Occupancy) / Peak Occupancy, expressed in percent (%). Its use is concentrated in Travel & tourism. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Seasonal occupancy variance measures demand swings across the year, and it is the strategic constraint of hospitality and resort economics - properties carry fixed capacity year-round, so shoulder-season utilization determines annual profitability more than peak-season performance. The strategic responses form a distinct playbook: demand smoothing (event programming, conference sales in low periods), differential pricing, and cost flexing (seasonal staffing) all attack the same problem from different angles. The variance metric deserves decomposition: weekday-versus-weekend and season-versus-season patterns suggest different fixes. Read with RevPAR seasonality decomposition, shoulder-season marketing ROI, staff cost flex ratio (how much cost actually varies with occupancy), and cash-flow timing management across the cycle.

## Formula

```
SOV = (Peak Occupancy - Off-Peak Occupancy) / Peak Occupancy
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** travel_tourism
- **Sector:** travel_tourism

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 934 (batch 3)
