# dea:metric-process-cost-per-transaction-deep-dive-ops

Candidate Performance Metric record for **Process Cost per Transaction (Deep Dive - Ops)** (PCPTD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-cost-per-transaction-deep-dive-ops`
- **Name:** Process Cost per Transaction (Deep Dive - Ops)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PCPTD

## 2. Definition

Process Cost per Transaction (Deep Dive - Ops) (PCPTD) addresses how efficiently resources are converted into outputs and is a fixture of operating model & process health deep dive reporting. The formula is Fully Loaded Cost / Process Transactions - reported in currency per unit. It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Fully Loaded Cost / Process Transactions
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** transformation
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operating_model_process_health_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3511 (batch 7)
