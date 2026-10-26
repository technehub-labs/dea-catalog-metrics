# dea:metric-actuarial-function-independence-rating

Candidate Performance Metric record for **Actuarial Function Independence Rating** (AFIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-actuarial-function-independence-rating`
- **Name:** Actuarial Function Independence Rating
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AFIR

## 2. Definition

A Actuarial & Reserving indicator, Actuarial Function Independence Rating (AFIR) quantifies conformance to standards, plans, or obligations. Its calculation is Regulatory Independence Assessment Score, measured in index (0-100 or normalized). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Insurance practice.

## 3. Context

Measures the independence of the actuarial function from commercial pressure - reporting lines, veto on assumptions, access to the board. Independence is the governance precondition for honest reserves and pricing in a business where profit is an estimate. Ratings that improve ahead of regulatory scrutiny deserve skepticism, and independence without competence is empty. Read with reserve development history and technical pricing uptake for behavioral evidence.

## Formula

```
Regulatory Independence Assessment Score
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** actuarial_reserving
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1538 (batch 6)
