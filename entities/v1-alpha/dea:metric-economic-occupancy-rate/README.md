# dea:metric-economic-occupancy-rate

Candidate Performance Metric record for **Economic Occupancy Rate** (EOR-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-economic-occupancy-rate`
- **Name:** Economic Occupancy Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EOR-E

## 2. Definition

Economic Occupancy Rate (EOR-E) addresses the economic value created or preserved and is a fixture of real estate portfolio & property management reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Collected Rent / Gross Potential Rent, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Real Estate.

## 3. Context

Measures occupied space's contribution at achieved rents, blending physical occupancy with rent actually being paid. It is the honest version of occupancy for investors because free rent, concessions, and tenants-in-dispute can leave a physically full building economically empty. Reconciliation of the two rates exposes concession depth and collection risk. Read with physical occupancy rate (Portfolio) and net effective rent per square metre.

## Formula

```
Collected Rent / Gross Potential Rent
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** real_estate_portfolio_property_management
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1739 (batch 6)
