# dea:metric-client-retention-rate-wealth

Candidate Performance Metric record for **Client Retention Rate (Wealth)** (CRR-W) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-client-retention-rate-wealth`
- **Name:** Client Retention Rate (Wealth)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRR-W

## 2. Definition

Within Wealth Management, Client Retention Rate (Wealth) (CRR-W) is used to gauge the retention of customers, users, or assets over time. Its calculation is Client Relationships Retained / Relationships at Start, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Wealth management practice.

## 3. Context

Client retention rate in wealth measures the share of client relationships (and often assets) staying year over year, and it is the compounding engine of the model - acquisition is expensive and slow (trust builds over years), so a wealth franchise's value is mostly its retention rate applied to an asset base that itself compounds. Retention needs asset-weighted and household-count versions read together: losing a few huge households while keeping hundreds of small ones can move assets materially while flattering count-based retention. The leading indicators are engagement (meetings attended, plan reviews completed) and life events (death, divorce, relocation create transition risk). Read with share of wallet (retained but disengaged clients are halfway out), advisor transition retention (client often follows the advisor), and complaint or service-failure history.

## Formula

```
CRR-W = Client Relationships Retained / Relationships at Start
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** retention
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1136 (batch 4)
