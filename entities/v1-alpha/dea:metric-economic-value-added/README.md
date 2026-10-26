# dea:metric-economic-value-added

Candidate Performance Metric record for **Economic Value Added** (EVA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-economic-value-added`
- **Name:** Economic Value Added
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EVA

## 2. Definition

Within Strategy & Portfolio, Economic Value Added (EVA) is used to gauge the economic value created or preserved. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as NOPAT - (Capital Employed x Cost of Capital), expressed in currency value. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Net operating profit after tax minus the full cost of the capital employed to earn it - the residual-income metric that management consultants (Stern Stewart's trademark) popularized as the single number that is unambiguously value creation, because a business only creates value when it earns more than its capital costs. Its strategic power is the change it forces in behavior: divisions charged for capital stop hoarding working capital and idle assets, which is why EVA programs famously surface surprising divestiture and inventory decisions. The concept's technical burden is the accounting adjustments - hundreds were proposed in the original framework to undo distortions - and the capital charge rate, which makes cross-company EVA comparisons fragile even when the headline arithmetic matches. As an internal steering metric it remains the cleanest insistence that capital is not free.

## Formula

```
NOPAT - (Capital Employed x Cost of Capital)
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** strategy
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** strategy_portfolio

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 370 (batch 1)
