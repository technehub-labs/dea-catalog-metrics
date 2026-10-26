# dea:metric-cash-buffer-days

Candidate Performance Metric record for **Cash Buffer Days** (CBD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cash-buffer-days`
- **Name:** Cash Buffer Days
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CBD

## 2. Definition

Cash Buffer Days (CBD) addresses exposure to adverse outcomes and is a fixture of treasury & cash management reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Cash and Liquid Reserves / Average Daily Cash Outflow, expressed in days. The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The number of days the organization could operate on current liquidity with no inflows - runway divided into operating days, and the survival arithmetic that made the metric the central number of the venture-backed company. Its strategic significance is decision pacing: hiring plans, expansion bets, and even marketing commitments are all sequenced against this number, and the classic operating rule of thumb - maintain enough buffer to reach the next milestone that unlocks funding - converts strategy into calendar. The honest computation uses the burn trend, not the burn snapshot, since burn that is rising shortens days faster than the linear math suggests. Read with the milestone dimension: the buffer number is only interpretable against what the organization needs to achieve before it hits zero, which is why the metric is always narrated as days-to-metric, never days alone.

## Formula

```
Cash and Liquid Reserves / Average Daily Cash Outflow
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** treasury_cash_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 594 (batch 2)
