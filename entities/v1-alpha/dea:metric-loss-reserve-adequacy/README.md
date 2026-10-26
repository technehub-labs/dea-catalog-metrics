# dea:metric-loss-reserve-adequacy

Candidate Performance Metric record for **Loss Reserve Adequacy** (LRA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-loss-reserve-adequacy`
- **Name:** Loss Reserve Adequacy
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LRA

## 2. Definition

Loss Reserve Adequacy (LRA) addresses exposure to adverse outcomes and is a fixture of actuarial & reserving reporting. It is computed as Reserves Held / Actuarial Best Estimate, expressed in ratio (x:1 or x). Its use is concentrated in Insurance. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Values outside the intended band, on either side, warrant investigation.

## 3. Context

An aggregate judgment measure - current reserves against expected ultimate losses - often expressed as a ratio with margin analysis. Adequacy is what regulators, auditors, and rating agencies interrogate, because under-reserving manufactures current profit at future expense. Beware adequacy claims resting on a single reserving method, and demand multiple-method triangulation with explicit margin rationale. Read with reserve development ratio and model backtesting pass rate (Actuarial).

## Formula

```
Reserves Held / Actuarial Best Estimate
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** actuarial_reserving
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1528 (batch 6)
