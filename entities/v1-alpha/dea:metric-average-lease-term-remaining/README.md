# dea:metric-average-lease-term-remaining

Candidate Performance Metric record for **Average Lease Term Remaining** (ALTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-lease-term-remaining`
- **Name:** Average Lease Term Remaining
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ALTR

## 2. Definition

Average Lease Term Remaining (ALTR) measures exposure to adverse outcomes in the Real Estate Portfolio & Property Management domain. The formula is Weighted Years Unexpired across Leases - reported in ratio (x:1 or x). It is a standard measure in the Real Estate sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures weighted average lease expiry across the portfolio. It is the stability-underwriting metric: longer WALT smooths re-leasing risk and supports debt capacity, but long WALT with below-market rents is a slow-bleed mark-to-market problem. Read alongside mark-to-market rent gap, since term and pricing interact in valuation. Read with tenant retention rate (Portfolio) and debt service coverage ratio (Property).

## Formula

```
Weighted Years Unexpired across Leases
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** real_estate_portfolio_property_management
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1744 (batch 6)
