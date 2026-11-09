# dea:metric-sale-price-to-list-price-ratio

Candidate Performance Metric record for **Sale Price to List Price Ratio** (SPLP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sale-price-to-list-price-ratio`
- **Name:** Sale Price to List Price Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SPLP

## 2. Definition

Sale Price to List Price Ratio (SPLP) measures the economic value created or preserved in the Real Estate Brokerage domain. The formula is Sale Price / Original List Price - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Real estate sector.

## 3. Context

Sale price to list price ratio measures the discount (or premium) achieved against asking price, and it is the negotiation-outcome metric of real estate transactions - buyers and sellers treat it as the market's verdict on pricing realism and negotiation skill. The ratio's diagnostic power comes from its direction and dispersion: ratios consistently above 100 percent signal competitive bidding (a seller's market), while wide dispersion signals inconsistent pricing quality across listings. The gaming risk is real on both sides: agents can list artificially low to engineer a bidding war (inflating the ratio while the seller still gets market price), so the ratio rewards pricing theater as much as pricing accuracy. Read with days on market (which reveals whether the ratio reflects market heat or pricing strategy), and final-versus-original list price comparison for the honest view.

## Formula

```
SPLP = Sale Price / Original List Price
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** real_estate_brokerage
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1012 (batch 3)
