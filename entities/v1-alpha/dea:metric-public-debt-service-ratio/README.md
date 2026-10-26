# dea:metric-public-debt-service-ratio

Candidate Performance Metric record for **Public Debt Service Ratio** (PDSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-public-debt-service-ratio`
- **Name:** Public Debt Service Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PDSR

## 2. Definition

Public Debt Service Ratio (PDSR) captures exposure to adverse outcomes for organizations tracking public sector & government. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Debt Service Payments / Government Revenue, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Public sector.

## 3. Context

Debt service payments as a share of revenue (or of exports, in the sovereign context) - the fiscal-capacity metric that lenders, rating agencies, and the debt-sustainability frameworks of the international financial institutions all treat as the primary sustainability signal, because it measures what the government owes against what it actually collects. Its strategic significance is the crowding-out arithmetic: every unit of revenue to debt service is a unit not available for the services and investment that justify the borrowing, and rising service ratios eventually force the choice between austerity, default, and monetization that defines fiscal crises. The honest read is rate-and-maturity aware: the ratio on current rates understates exposure for debt that must refinance at higher rates, and the maturity schedule - not the current service ratio - is what dates the pressure. Read with the currency-denomination split, since foreign-currency debt service depends on exchange-rate policy rather than domestic revenue effort, a distinction that changes the risk entirely.

## Formula

```
PDSR = Debt Service Payments / Government Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** public_sector_government
- **Sector:** public_sector

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 644 (batch 2)
