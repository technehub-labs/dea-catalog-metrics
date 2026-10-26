# dea:metric-athlete-availability-rate-deep-dive

Candidate Performance Metric record for **Athlete Availability Rate (Deep Dive)** (AAR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-athlete-availability-rate-deep-dive`
- **Name:** Athlete Availability Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AAR-D

## 2. Definition

Athlete Availability Rate (Deep Dive) (AAR-D) addresses the utilization or availability of capacity and is a fixture of sports clubs & leagues (deep dive) reporting. Its calculation is Matches Available per Player / Squad Matches, measured in percent (%). It originates from and is most used in Sports practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of squad available for selection, weighting by player importance. Availability is the direct input to competitive performance, and modern clubs manage it as an asset metric - squad cost is wasted when high earners are unavailable. Importance weighting is the honest-read question, since simple headcount availability can look healthy while the spine of the team is injured. Read with injury burden rate (Deep Dive) and squad-cost-per-available-player economics.

## Formula

```
Matches Available per Player / Squad Matches
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** sports_clubs_leagues_deep_dive
- **Sector:** sports

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1997 (batch 6)
