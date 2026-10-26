# dea:metric-litigation-win-rate

Candidate Performance Metric record for **Litigation Win Rate** (LWR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-litigation-win-rate`
- **Name:** Litigation Win Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LWR

## 2. Definition

Litigation Win Rate (LWR) captures how effectively a process or entity achieves its intended outcome for organizations tracking legal. It is defined as Favorable Outcomes / Cases Concluded; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The share of resolved matters ending favorably - the outcome metric of the legal function, given strategic meaning by its connection to the settlement-leverage question: a credible trial record shifts settlement dynamics for the entire docket, since counterparties price the likelihood of facing a firm that actually litigates. The metric demands case-mix honesty to mean anything - win rate on commercial disputes, employment matters, and IP cases follow different base rates, and a blended rate moves with docket mix as much as with legal skill. Read with cost-per-matter and time-to-resolution, since a high win rate achieved through scorched-earth spending may be worse economics than a lower rate with early favorable settlements. The denominator choice matters most: excluding settled matters flatters the rate with the cases that were never strong enough to fight.

## Formula

```
Favorable Outcomes / Cases Concluded
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** legal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 390 (batch 1)
