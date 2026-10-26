# dea:metric-system-average-interruption-duration-index

Candidate Performance Metric record for **System Average Interruption Duration Index** (SAIDI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-system-average-interruption-duration-index`
- **Name:** System Average Interruption Duration Index
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SAIDI

## 2. Definition

System Average Interruption Duration Index (SAIDI) measures the quality of outputs and outcomes in the Energy & Utilities domain. Its calculation is Total Customer Interruption Minutes / Total Customers Served, measured in minutes. It originates from and is most used in Energy & utilities practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

The average minutes of sustained outage each customer experiences per year - the customer-experience half of the IEEE 1366 reliability pair, and the number customers actually remember, since duration is the inconvenience. Its strategic weight is the same regulatory linkage as SAIFI but with sharper investment content: duration is dominated by restoration speed (crew response, switching capability, fault location), and modern grid investment - automated switches, self-healing feeder sections, better fault isolation - attacks this metric specifically, which is why automation business cases quote SAIDI-minutes saved per dollar. Read the two indexes together: falling SAIDI with flat SAIFI means faster restoration; falling SAIFI drags SAIDI down with it because customers are never interrupted. Both patterns are wins, but they imply different asset strategies.

## Formula

```
Total Customer Interruption Minutes / Total Customers Served
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_utilities
- **Sector:** energy_utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 437 (batch 1)
