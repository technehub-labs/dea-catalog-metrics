# dea:metric-momentary-average-interruption-frequency-index

Candidate Performance Metric record for **Momentary Average Interruption Frequency Index** (MAIFI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-momentary-average-interruption-frequency-index`
- **Name:** Momentary Average Interruption Frequency Index
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MAIFI

## 2. Definition

Momentary Average Interruption Frequency Index (MAIFI) measures the quality of outputs and outcomes in the Utilities Field Operations & Grid domain. It is computed as Momentary Interruptions / Customers Served, expressed in times per period. Its use is concentrated in Utilities. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

MAIFI, from IEEE Std 1366, counts momentary interruptions (under five minutes, typically recloser operations) per customer per year. Momentaries matter because they drive the biggest single source of customer complaints - blinking clocks and dropped equipment - even though they barely register in SAIDI. Utilities with high MAIFI and decent SAIDI often have aggressive reclosing schemes that restore the feeder quickly but at customers' annoyance expense; the fix is targeted equipment replacement or single-phase reclosing, not blanket policy.

## Formula

```
Momentary Interruptions / Customers Served
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** utilities_field_operations_grid
- **Sector:** utilities

## Attribution

- **Source credit:** IEEE Std 1366 reliability indices

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1885 (batch 6)
