# dea:metric-cost-to-collect

Candidate Performance Metric record for **Cost to Collect** (CTC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-to-collect`
- **Name:** Cost to Collect
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CTC

## 2. Definition

A Healthcare Revenue Cycle indicator, Cost to Collect (CTC) quantifies how efficiently resources are converted into outputs. It is defined as Total Revenue Cycle Cost / Collected Revenue; the result is stated in percent (%). In Healthcare, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Cost to collect measures revenue-cycle operating expense as a share of net patient revenue, and it is the efficiency metric that healthcare financial leadership benchmarks relentlessly - high performers run revenue-cycle cost at 2-3 percent of net revenue while less mature operations spend double or more. The cost pools are distinctive: billing staff, coding, payer follow-up, vendor software, and outsourcing contracts, and the strategic question is insourcing versus outsourcing economics, which are more balanced than vendor pitches suggest. Cost must be read against collection quality - a cheap cycle that writes off denials unappealed is expensive in net-revenue terms. Read with cost per claim or per encounter, denial write-off rates (the hidden cost of under-resourcing), self-service and automation adoption rates, and staff productivity metrics per claim touched.

## Formula

```
Total Revenue Cycle Cost / Collected Revenue
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** healthcare_revenue_cycle
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 875 (batch 3)
