# dea:metric-franchisee-retention-rate

Candidate Performance Metric record for **Franchisee Retention Rate** (FRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-franchisee-retention-rate`
- **Name:** Franchisee Retention Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FRR

## 2. Definition

A Franchise & Multi-site indicator, Franchisee Retention Rate (FRR) quantifies the retention of customers, users, or assets over time. It is computed as Franchisees Renewing or Continuing / Franchisees, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Franchise & multi-site.

## 3. Context

Franchisee retention measures the share of franchisees remaining in the system year-over-year, and it is the franchising model's structural integrity check - the system only works if franchisees make money, and franchisee failure is both revenue loss and reputational damage that suppresses future unit sales. Retention must be read alongside unit economics: franchisees who survive but struggle create a different problem (underperforming units, deferred maintenance, brand erosion) than those who exit cleanly. Turnover clusters signal systemic issues - territory saturation, supply-chain cost increases, or franchisor fee creep. Read with franchisee profitability distribution (not just survival), franchise agreement renewal rates at the 10-year mark, and franchisor-franchisee litigation or dispute counts.

## Formula

```
FRR = Franchisees Renewing or Continuing / Franchisees
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** franchise_multi_site
- **Sector:** franchise_multi_site

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 805 (batch 2)
