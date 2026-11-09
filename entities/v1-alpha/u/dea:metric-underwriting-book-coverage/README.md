# dea:metric-underwriting-book-coverage

Candidate Performance Metric record for **Underwriting Book Coverage** (UBC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-underwriting-book-coverage`
- **Name:** Underwriting Book Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** UBC

## 2. Definition

A Investment Banking & Capital Markets indicator, Underwriting Book Coverage (UBC) quantifies exposure to adverse outcomes. The formula is Order Book Value / Offering Value - reported in ratio (x:1 or x). It is a standard measure in the Investment banking sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of potential deals or mandates actually pursued across the book. It matters because coverage determines whether the bank sees the deal flow it should. Teams can inflate coverage by quoting on unpursued opportunities. Read with League Table rankings and fee revenue to confirm coverage converts into won mandates.

## Formula

```
UBC = Order Book Value / Offering Value
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_banking_capital_markets
- **Sector:** investment_banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1148 (batch 4)
