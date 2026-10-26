# dea:metric-net-new-assets-growth

Candidate Performance Metric record for **Net New Assets Growth** (NNAG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-new-assets-growth`
- **Name:** Net New Assets Growth
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NNAG

## 2. Definition

Within Wealth Management, Net New Assets Growth (NNAG) is used to gauge growth over time. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Net New Client Assets / Assets under Management at Start, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Wealth management practice.

## 3. Context

Net new assets growth measures the net inflow of client money into a wealth platform - new deposits minus withdrawals - and it is the growth engine that separates a wealth manager whose AUM rise merely rides market performance from one that is genuinely winning clients. NNA is the honest growth metric because market beta inflates AUM without any commercial achievement, so investors and valuation analysts strip it out. The decomposition matters: gross flows minus redemptions reveals whether growth is acquisition-driven (new money, often transitory) or retention-driven (durable compounding). Read with client retention rate, flow persistence by segment, and revenue yield on new assets since not all assets carry the same fee level.

## Formula

```
NNAG = Net New Client Assets / Assets under Management at Start
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** wealth_management
- **Sector:** wealth_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1134 (batch 4)
