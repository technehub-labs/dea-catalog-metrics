# dea:metric-share-of-wallet-wealth

Candidate Performance Metric record for **Share of Wallet (Wealth)** (SOW-W) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-share-of-wallet-wealth`
- **Name:** Share of Wallet (Wealth)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SOW-W

## 2. Definition

Share of Wallet (Wealth) (SOW-W) addresses growth over time and is a fixture of wealth management reporting. The formula is Assets Held with Firm / Client Estimated Total Assets - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Wealth management sector.

## 3. Context

Share of wallet measures the proportion of a client's total investable assets held with the firm, and it is the expansion metric that matters more than acquisition in a mature wealth market - the cheapest growth is deepening relationships you already won. Its honest measurement is hard because total client assets are only partially observable (outside-account assets require disclosure or estimation), so firms rely on declared assets, data enrichment, and inference. The drivers are segment fit (clients consolidate where the offering covers their needs - lending, planning, estate) and advisor proactivity in asking. Read with assets-under-management per household trend, product penetration counts, and consolidation triggers (life events) versus organic drift.

## Formula

```
Assets Held with Firm / Client Estimated Total Assets
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** wealth_management
- **Sector:** wealth_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1137 (batch 4)
