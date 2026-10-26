# dea:metric-per-match-operating-cost

Candidate Performance Metric record for **Per-Match Operating Cost** (PMOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-per-match-operating-cost`
- **Name:** Per-Match Operating Cost
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PMOC

## 2. Definition

Per-Match Operating Cost (PMOC) addresses how efficiently resources are converted into outputs and is a fixture of sports clubs & leagues (deep dive) reporting. The formula is Stadium Operating Costs / Matches - reported in currency value. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Lower values are better; each reduction is an improvement. It is a standard measure in the Sports sector.

## Formula

```
PMOC = Stadium Operating Costs / Matches
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** sports_clubs_leagues_deep_dive
- **Sector:** sports

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2005 (batch 6)
