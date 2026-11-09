# dea:metric-aged-receivables-ratio-property

Candidate Performance Metric record for **Aged Receivables Ratio (Property)** (ARR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-aged-receivables-ratio-property`
- **Name:** Aged Receivables Ratio (Property)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ARR-P

## 2. Definition

Aged Receivables Ratio (Property) (ARR-P) addresses exposure to adverse outcomes and is a fixture of real estate portfolio & property management reporting. Its calculation is Rent Over 60 Days / Total Rent Receivable, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Real Estate practice.

## Formula

```
ARR-P = Rent Over 60 Days / Total Rent Receivable
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** real_estate_portfolio_property_management
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1758 (batch 6)
