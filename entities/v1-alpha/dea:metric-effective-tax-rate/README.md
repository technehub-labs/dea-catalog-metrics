# dea:metric-effective-tax-rate

Candidate Performance Metric record for **Effective Tax Rate** (ETR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-effective-tax-rate`
- **Name:** Effective Tax Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ETR

## 2. Definition

Effective Tax Rate (ETR) captures conformance to standards, plans, or obligations for organizations tracking tax & fiscal. It is computed as Total Tax Expense / Pre-Tax Accounting Income, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Total tax expense over pre-tax accounting profit - the realized tax burden that reconciles the statutory rate with what the company actually pays, and the number whose movements between the two tell the entire tax-strategy story. Its strategic significance is the disclosure intensity it now carries: public country-by-country reporting and the global minimum-tax regime have compressed the space where rate gaps could quietly live, and an effective rate that diverges persistently from statutory mix signals either genuine structural attributes (losses, credits, timing) or aggressive positions, which the market prices as risk. The honest read separates the recurring structure from the one-offs: rate movements from discrete items and from disputes resolving in the period are noise, and the sustainable rate is the number guidance should rest on. Read with the cash-tax rate alongside, since the gap between book and cash tax is the timing exposure that eventually reverses.

## Formula

```
Total Tax Expense / Pre-Tax Accounting Income
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** tax_fiscal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 604 (batch 2)
