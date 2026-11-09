# dea:metric-time-to-market

Candidate Performance Metric record for **Time to Market** (TTM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-market`
- **Name:** Time to Market
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TTM

## 2. Definition

A R&D and Innovation indicator, Time to Market (TTM) quantifies how efficiently resources are converted into outputs. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Days from Concept Approval to First Sale, expressed in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Elapsed time from concept approval to launch - the velocity metric of product development, and strategically the one with the sharpest asymmetry: being late to market costs share and price premium that launch excellence can never recover, which is the finding the development-literature tradition (Cooper and the cycle-time research) established as the product management consensus. Its significance is compounding: in markets with short product lifecycles, each cycle missed shortens the revenue runway of everything downstream, and serial delay compounds into generational lag. The honest measurement has clean start and end conventions - projects measured from funding, staffed, and concept-approved start points differ by quarters - and the metric punishes queue time more than work time, which is why development-velocity programs that add resources rarely move it while those that remove approval queues do.

## Formula

```
TTM = Days from Concept Approval to First Sale
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** r_d_and_innovation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 538 (batch 1)
