# dea:metric-piotroski-f-score

Candidate Performance Metric record for **Piotroski F-Score** (PIOF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-piotroski-f-score`
- **Name:** Piotroski F-Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PIOF

## 2. Definition

Piotroski F-Score (PIOF) addresses the quality of outputs and outcomes and is a fixture of valuation & corporate finance standard measures reporting. Its calculation is Count of Nine Fundamental Strength Signals Met, measured in score (points). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The Piotroski F-Score, from Joseph D. Piotroski (2000), checks nine binary signals across profitability, leverage/liquidity, and operating efficiency - one point each. Scores 8-9 flag fundamentally strong value stocks, 0-2 weak ones; Piotroski's research showed high-F value stocks materially outperformed. It was designed specifically to separate value-trap survivors from deteriorating cheap stocks, so it is most informative on a low-valuation screening universe, and it is a once-a-year balance-sheet snapshot rather than a timing tool.

## Formula

```
PIOF = Count of Nine Fundamental Strength Signals Met
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** valuation_corporate_finance_standard_measures

## Attribution

- **Source credit:** Joseph D. Piotroski, 2000

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4036 (batch 9)
