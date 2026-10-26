# dea:metric-cost-per-unit-produced

Candidate Performance Metric record for **Cost per Unit Produced** (CPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-unit-produced`
- **Name:** Cost per Unit Produced
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPU

## 2. Definition

Cost per Unit Produced (CPU) addresses how efficiently resources are converted into outputs and is a fixture of operations reporting. It is computed as Total Production Cost / Units Produced, expressed in currency per unit. It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures total production cost divided by good units produced. It matters as the clearest single read on production efficiency and pricing headroom. Teams can cut it cosmetically by deferring maintenance, running over-sized batches, or reclassifying scrap costs elsewhere. Read with Scrap Cost Percentage and Energy Cost per Unit to confirm unit-cost gains are structural, not deferred waste.

## Formula

```
Total Production Cost / Units Produced
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 166 (batch 1)
