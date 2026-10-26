# dea:metric-market-share

Candidate Performance Metric record for **Market Share** (MSH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-market-share`
- **Name:** Market Share
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MSH

## 2. Definition

Market Share (MSH) measures growth over time in the Strategy & Portfolio domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Organization Sales / Total Market Sales - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The organization's share of the total addressable market - by revenue or volume - the classic competitive-position metric that strategy has tracked since the market-share-versus-ROI findings of the PIMS program made leadership position a value in itself. Strategic use is the experience-curve logic: share leaders accumulate cost advantages through scale and learning, which funds either margin or price aggression, and the flywheel is why share is contested so fiercely in maturing markets. The measurement battleground is market definition: a firm can lead the market it defines and trail the one its customers experience, so segment-boundary choices deserve as much scrutiny as the number. Read share with growth: gaining share in a shrinking market and losing share in a booming one can look identical in revenue.

## Formula

```
Organization Sales / Total Market Sales
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** growth
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** strategy_portfolio

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 364 (batch 1)
