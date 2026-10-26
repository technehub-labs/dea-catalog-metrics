# dea:metric-maximum-drawdown

Candidate Performance Metric record for **Maximum Drawdown** (MDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maximum-drawdown`
- **Name:** Maximum Drawdown
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MDD

## 2. Definition

Maximum Drawdown (MDD) measures exposure to adverse outcomes in the Investment Management domain. It is computed as (Peak Value - Trough Value) / Peak Value, expressed in percent (%). Its use is concentrated in Asset management. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Maximum drawdown is the peak-to-trough decline in portfolio value - the worst loss an investor actually experienced, not a statistical abstraction. That concreteness is why it anchors risk management and marketing disclosures alike: an 8 percent annual return achieved through a 45 percent drawdown is a fundamentally different product than the same return with a 12 percent drawdown, because investors behave badly at the trough, and drawdown is where forced selling and capitulation occur. Path dependency is its defining trait: it cannot be averaged away across periods. Read with time-to-recovery (how long to claw back to peak) and Calmar ratio, which normalizes return by drawdown severity.

## Formula

```
(Peak Value - Trough Value) / Peak Value
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management
- **Sector:** asset_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 767 (batch 2)
