# dea:metric-bid-win-rate

Candidate Performance Metric record for **Bid Win Rate** (BWR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bid-win-rate`
- **Name:** Bid Win Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BWR

## 2. Definition

Bid Win Rate (BWR) addresses growth over time and is a fixture of construction & engineering reporting. The formula is Bids Won / Bids Submitted - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Construction & engineering sector.

## 3. Context

Won bids as a share of bids submitted - the conversion metric of the construction and engineering business model, whose strategic significance follows from the tender economics: bidding is expensive (estimating, proposal, and pursuit costs are real overhead), so win rate against cost-to-bid determines whether the pipeline is affordable, and win rates below the break-even threshold make every additional bid a cost. The analysis that matters is decomposed: win rate by client, project type, size band, and competitor set reveals where the firm genuinely competes versus where it bids to appear busy - the discipline that separates contractors who choose work from contractors who accept it. Read with margin-at-bid and margin-at-completion: a win rate bought with underpriced bids is volume with negative economics, and the win-rate-versus-margin trade is the central strategic dial of the tendering business.

## Formula

```
BWR = Bids Won / Bids Submitted
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** construction_engineering
- **Sector:** construction_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 672 (batch 2)
