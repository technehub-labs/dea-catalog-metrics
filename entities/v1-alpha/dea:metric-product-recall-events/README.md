# dea:metric-product-recall-events

Candidate Performance Metric record for **Product Recall Events** (PRE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-product-recall-events`
- **Name:** Product Recall Events
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PRE

## 2. Definition

A Agriculture & Food Processing indicator, Product Recall Events (PRE) quantifies exposure to adverse outcomes. The formula is Food Product Recalls per Period - reported in count (items per period). It is a standard measure in the Agriculture & food sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Product recall events count the number of times product must be retrieved from the market, and while a raw count seems binary, each event carries a distinctive cost signature - notification, logistics, destruction, regulatory penalties, and reputational damage that dwarfs the direct cost. Trend matters more than absolute count: a single well-managed recall signals different risk than a pattern of escalating ones. Root-cause distribution is the real intelligence - allergen labeling recurring suggests a systemic labeling control failure, not random bad luck. Read with traceability coverage and recall mock-drill performance, since traceability speed determines whether a recall is targeted or blanket.

## Formula

```
Food Product Recalls per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agriculture_food_processing
- **Sector:** agriculture_food

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 731 (batch 2)
