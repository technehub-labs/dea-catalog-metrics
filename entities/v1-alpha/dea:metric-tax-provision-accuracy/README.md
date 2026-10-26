# dea:metric-tax-provision-accuracy

Candidate Performance Metric record for **Tax Provision Accuracy** (TPA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tax-provision-accuracy`
- **Name:** Tax Provision Accuracy
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TPA

## 2. Definition

Tax Provision Accuracy (TPA) addresses the quality of outputs and outcomes and is a fixture of tax & fiscal reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is 1 - ABS(Provision - Final Liability) / Final Liability, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how closely booked tax provisions match final tax liabilities. It matters because provision error distorts earnings and signals control weakness. Teams can smooth accuracy by adjusting prior-period comparisons instead of fixing estimation. Read with Effective Tax Rate variance analysis and Tax Audit Adjustment Ratio to confirm the provision process is disciplined.

## Formula

```
1 - ABS(Provision - Final Liability) / Final Liability
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** tax_fiscal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 606 (batch 2)
