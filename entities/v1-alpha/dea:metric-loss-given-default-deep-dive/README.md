# dea:metric-loss-given-default-deep-dive

Candidate Performance Metric record for **Loss Given Default (Deep Dive)** (LGDDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-loss-given-default-deep-dive`
- **Name:** Loss Given Default (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LGDDD

## 2. Definition

Loss Given Default (Deep Dive) (LGDDD) addresses exposure to adverse outcomes and is a fixture of credit & collections risk (enterprise) reporting. It is computed as Expected Loss after Recovery / Exposure at Default, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of exposure lost if default occurs, after recoveries. LGD drives both pricing and provisioning, and it is the least stable parameter. Recovery assumptions based on boom-period collateral values collapse in downturns. Read with recovery rate on charged-off (Deep Dive) and collateral coverage ratio.

## Formula

```
Expected Loss after Recovery / Exposure at Default
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** credit_collections_risk_enterprise

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4196 (batch 9)
