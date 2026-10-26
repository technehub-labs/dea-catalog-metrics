# dea:metric-league-table-rank

Candidate Performance Metric record for **League Table Rank** (LTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-league-table-rank`
- **Name:** League Table Rank
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LTR

## 2. Definition

A Investment Banking & Capital Markets indicator, League Table Rank (LTR) quantifies growth over time. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Rank in Deal Volume or Fee League Tables - reported in count (items per period). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Investment banking sector.

## 3. Context

League table rank measures a bank's position in deal-volume or fee rankings (M&A, equity and debt underwriting), and it is the reputation-asset metric of investment banking - the tables are published continuously and studied by clients and talent alike, because rank is self-reinforcing: top-ranked banks win pitches on brand, attract the best bankers, and get first calls on mandates. The metric's honesty issue is inclusion criteria: table compilers differ on which deals count (deal types, announced versus completed, sole versus joint credit), and banks game category definitions relentlessly. Rank is a positioning metric, not a profitability one - volume leadership at compressed fees is a losing game. Read with fee share versus volume share (the profitable divergence), rank by product and region, and pitch-win trend which is the underlying driver.

## Formula

```
Rank in Deal Volume or Fee League Tables
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1144 (batch 4)
