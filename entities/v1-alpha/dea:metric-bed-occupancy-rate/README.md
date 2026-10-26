# dea:metric-bed-occupancy-rate

Candidate Performance Metric record for **Bed Occupancy Rate** (BOR2) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bed-occupancy-rate`
- **Name:** Bed Occupancy Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BOR2

## 2. Definition

Within Healthcare, Bed Occupancy Rate (BOR2) is used to gauge the utilization or availability of capacity. It is computed as Occupied Bed Days / Available Bed Days, expressed in percent (%). Its use is concentrated in Healthcare. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Values outside the intended band, on either side, warrant investigation.

## 3. Context

The share of staffed beds occupied - the capacity metric of the hospital, and one of the few operational numbers where both high and low readings are problems: occupancy too low wastes fixed capacity in a business of tight margins, while occupancy persistently near full removes the slack that absorbs arrival variability, which queueing logic says converts directly into waits, corridor patients, and diversion. The strategic significance is the target band: the operations-research understanding that flow requires buffer is why hospitals aim at the low-nineties rather than the high nineties, and the discipline of that aim is the operational conversation. Read with the turnover dimension: occupancy measured at midnight (the conventional census snapshot) understates the day's true work - beds can be occupied by different patients in the same day, which turnover-interval metrics capture and census-based occupancy hides.

## Formula

```
Occupied Bed Days / Available Bed Days
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** healthcare
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 461 (batch 1)
