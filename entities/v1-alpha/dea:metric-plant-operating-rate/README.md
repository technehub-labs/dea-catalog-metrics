# dea:metric-plant-operating-rate

Candidate Performance Metric record for **Plant Operating Rate** (POR-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-plant-operating-rate`
- **Name:** Plant Operating Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** POR-C

## 2. Definition

A Chemicals indicator, Plant Operating Rate (POR-C) quantifies the utilization or availability of capacity. It is defined as Actual Production / Nameplate Capacity; the result is stated in percent (%). In Chemicals, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Plant operating rate measures chemical production against nameplate capacity, and it is the supply-demand barometer of the chemicals cycle - rates above 90 percent typically signal a tight market with pricing power, while rates in the 70s signal oversupply, since this capital-intensive industry needs high utilization to cover enormous fixed costs. The reliability distinction matters: operating rate can be high because demand is strong or because a competitor's outage absorbed the supply - so it is a market-level signal more than a plant-level performance one. Scheduled turnaround cadence and unplanned outage frequency drive the plant-level measure. Read with industry-level operating rates by product line, planned versus unplanned downtime, and margin per tonne which combines utilization with spread capture.

## Formula

```
Actual Production / Nameplate Capacity
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** chemicals
- **Sector:** chemicals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 896 (batch 3)
