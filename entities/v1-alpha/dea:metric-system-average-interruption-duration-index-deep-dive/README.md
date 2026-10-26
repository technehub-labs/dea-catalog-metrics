# dea:metric-system-average-interruption-duration-index-deep-dive

Candidate Performance Metric record for **System Average Interruption Duration Index (Deep Dive)** (SAIDI-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-system-average-interruption-duration-index-deep-dive`
- **Name:** System Average Interruption Duration Index (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SAIDI-D

## 2. Definition

System Average Interruption Duration Index (Deep Dive) (SAIDI-D) addresses the quality of outputs and outcomes and is a fixture of utilities field operations & grid reporting. It is computed as Customer-Minutes Interrupted / Customers Served, expressed in minutes. Its use is concentrated in Utilities. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

SAIDI, from IEEE Std 1366, is the average customer-minutes of sustained interruption per customer served per year - the standard reliability measure utilities report to regulators. Utilities typically separate major-event days (MED) using the IEEE 2.5-beta method so storms do not drown out everyday performance. Typical US values range roughly from under 100 to over 300 minutes; drive it down through feeder automation, tree trimming, and looped topologies, and remember it weights all customers equally - pair with CAIDI and SAIFI to see duration versus frequency.

## Formula

```
Customer-Minutes Interrupted / Customers Served
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** utilities_field_operations_grid
- **Sector:** utilities

## Attribution

- **Source credit:** IEEE Std 1366 reliability indices

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1882 (batch 6)
