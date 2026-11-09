# dea:metric-win-rate-investments

Candidate Performance Metric record for **Win Rate (Investments)** (WRI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-win-rate-investments`
- **Name:** Win Rate (Investments)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WRI

## 2. Definition

Win Rate (Investments) (WRI) addresses how effectively a process or entity achieves its intended outcome and is a fixture of investment management reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Profitable Positions Closed / Positions Closed, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Asset management practice.

## 3. Context

Win rate is the share of closed positions that were profitable, and it is dangerously incomplete alone - a 90 percent win rate with losses averaging 10 times the size of gains still loses money, which is exactly why trend-following funds survive with 35-40 percent win rates and large asymmetric payoffs. Its value comes in decomposition: win rate must be read with average win-to-average loss ratio to produce expectancy, and with holding period, since short-term high win-rate strategies often hide negative convexity. Also beware closed-position bias: open losing positions excluded from the sample flatter the number. Read with profit factor and expectancy per trade for the complete picture.

## Formula

```
WRI = Profitable Positions Closed / Positions Closed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** effectiveness
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 768 (batch 2)
