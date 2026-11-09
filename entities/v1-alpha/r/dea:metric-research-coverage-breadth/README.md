# dea:metric-research-coverage-breadth

Candidate Performance Metric record for **Research Coverage Breadth** (RCB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-research-coverage-breadth`
- **Name:** Research Coverage Breadth
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RCB

## 2. Definition

Research Coverage Breadth (RCB) measures the economic value created or preserved in the Investment Banking & Capital Markets domain. Its calculation is Companies under Research Coverage, measured in count (items per period). It originates from and is most used in Investment banking practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Research coverage breadth measures the number of companies and sectors under coverage, and it is the franchise-infrastructure metric of sell-side research - coverage is what earns analysts the corporate-access and idea-flow relationships that generate trading and banking revenue, so breadth is the footprint within which the whole model operates. The strategic tension is breadth versus depth: scarce senior-analyst time spread across many names dilutes insight quality, and the industry has been shrinking coverage lists (post-MiFID II unbundling especially) toward fewer, higher-conviction names. The honest metric pairs coverage count with engagement quality - client note readership, corporate-access requests, and vote rankings. Read with revenue per covered name (the profitability of the footprint), coverage churn (initiating and dropping names), and vote-penetration among institutional clients.

## Formula

```
RCB = Companies under Research Coverage
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_banking_capital_markets
- **Sector:** investment_banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1152 (batch 4)
