# dea:metric-cash-conversion-cycle-deep-dive

Candidate Performance Metric record for **Cash Conversion Cycle (Deep Dive)** (CCC-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cash-conversion-cycle-deep-dive`
- **Name:** Cash Conversion Cycle (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CCC-D

## 2. Definition

Cash Conversion Cycle (Deep Dive) (CCC-D) measures how efficiently resources are converted into outputs in the Corporate Treasury (Deep Dive) domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as DIO + DSO - DPO, expressed in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures days from cash out (inventory, payables) to cash in (receivables). CCC is the working-capital efficiency metric that connects operations to cash: every day removed releases funding permanently, which is why supply chain programs sell themselves in CCC terms. Improvement must be read for risk transfer - stretched payables that strain suppliers convert efficiency into supply fragility. Read with DSO, DPO, and DIO components for where the change actually came from.

## Formula

```
DIO + DSO - DPO
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_treasury_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2182 (batch 6)
