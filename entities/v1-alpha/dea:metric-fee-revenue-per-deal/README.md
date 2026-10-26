# dea:metric-fee-revenue-per-deal

Candidate Performance Metric record for **Fee Revenue per Deal** (FRPD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fee-revenue-per-deal`
- **Name:** Fee Revenue per Deal
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FRPD

## 2. Definition

Fee Revenue per Deal (FRPD) captures the economic value created or preserved for organizations tracking investment banking & capital markets. Its calculation is Total Advisory and Underwriting Fees / Deals Closed, measured in currency value. It originates from and is most used in Investment banking practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Fee revenue per deal measures average economics per completed transaction, and it is the pricing-power metric of advisory and underwriting - the same league-table position can be built on full-fee premium mandates or discounted volume, and only this metric tells them apart. Fee per deal decomposes into deal size mix, fee-rate discipline (percentage of deal value captured), and product mix (M&A advisory, ECM, DCM each carry different economics). The trend reveals competitive pressure: declining fee per deal at constant deal size is fee compression, a well-documented industry pattern driven by competing banks and in-house corporate development teams. Read with fee-rate by deal type, win rate versus fee trade-offs (winning by discounting shows up here first), and revenue per banker as the productivity translation.

## Formula

```
Total Advisory and Underwriting Fees / Deals Closed
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_banking_capital_markets
- **Sector:** investment_banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1145 (batch 4)
