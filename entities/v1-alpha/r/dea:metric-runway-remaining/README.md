# dea:metric-runway-remaining

Candidate Performance Metric record for **Runway Remaining** (RWR-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-runway-remaining`
- **Name:** Runway Remaining
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RWR-S

## 2. Definition

A Startup & Venture-Backed Business indicator, Runway Remaining (RWR-S) quantifies exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Cash Available / Net Monthly Burn, expressed in months. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures months of cash available at current burn. It is the existential metric of venture-backed companies: every strategic decision, hiring plan, and negotiation position is priced off runway, and the metric forces the honesty that income statements defer. Runway computed on optimistic revenue assumptions is self-deception with a number attached, so stress-read at reduced-collection scenarios. Read with burn multiple and CAC payback period (Deep Dive).

## Formula

```
RWR-S = Cash Available / Net Monthly Burn
```

## Unit

- **Unit reference:** `dea:unit-month`
- **Unit:** month
- **Unit label (as published):** months

## Classification

- **Subject classification:** strategy
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** startup_venture_backed_business

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2442 (batch 6)
