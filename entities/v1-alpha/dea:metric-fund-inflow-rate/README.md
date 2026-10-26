# dea:metric-fund-inflow-rate

Candidate Performance Metric record for **Fund Inflow Rate** (FIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fund-inflow-rate`
- **Name:** Fund Inflow Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FIR

## 2. Definition

Fund Inflow Rate (FIR) addresses growth over time and is a fixture of investment management reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Net New Investor Flows / Assets under Management, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Asset management.

## 3. Context

Fund inflow rate measures net new capital entering a fund as a share of beginning assets, and it is the growth engine of the asset management business model - management fees scale with AUM, so flows are revenue. The critical subtlety is performance-flow asymmetry: strong performance attracts inflows slowly, while poor performance triggers outflows sharply, creating convexity that punishes drawdowns twice. Flows also drive fund behavior at scale - large inflows force position sizing compromises and can dilute the strategy that attracted flows in the first place. Read with flow persistence (is the same client segment adding repeatedly?), redemption rates, and capacity utilization.

## Formula

```
Net New Investor Flows / Assets under Management
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management
- **Sector:** asset_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 772 (batch 2)
