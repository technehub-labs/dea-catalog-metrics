# dea:metric-working-capital-efficiency

Candidate Performance Metric record for **Working Capital Efficiency** (WCE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-working-capital-efficiency`
- **Name:** Working Capital Efficiency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WCE

## 2. Definition

Within Treasury & Cash Management, Working Capital Efficiency (WCE) is used to gauge how efficiently resources are converted into outputs. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Revenue / (Current Assets - Current Liabilities); the result is stated in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The productivity of the cash tied up in operations - conventionally tracked as revenue or cost of sales per unit of net working capital, or through the cycle-time family (inventory, receivable, and payable days). Its strategic significance is the funding relationship: growth consumes working capital, and businesses that cannot finance their own growth cycle fund it with debt or starve it - which is why this metric decides whether growth is self-financing. The honest analysis decomposes the cycle, since each component moves for different reasons and some improvements are value transfers rather than value creation: stretching payables is borrowing from suppliers, and shrinking receivables by factoring is borrowing from a bank at a worse rate, both of which look like efficiency. The economically real improvements - faster inventory turns from genuine process velocity, faster collection from billing accuracy - are the ones that compound.

## Formula

```
WCE = Revenue / (Current Assets - Current Liabilities)
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** treasury_cash_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 602 (batch 2)
