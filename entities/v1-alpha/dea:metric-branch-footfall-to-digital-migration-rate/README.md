# dea:metric-branch-footfall-to-digital-migration-rate

Candidate Performance Metric record for **Branch Footfall to Digital Migration Rate** (BFDM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-branch-footfall-to-digital-migration-rate`
- **Name:** Branch Footfall to Digital Migration Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BFDM

## 2. Definition

Branch Footfall to Digital Migration Rate (BFDM) measures how efficiently resources are converted into outputs in the Retail Banking Branch Network (Deep Dive) domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Migrated Transactions / Addressable Branch Transactions, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Banking.

## 3. Context

Measures the shift of branch transactions to digital channels. It is the demand-side evidence behind branch rationalization, and it must be read with customer-segment equity: migration of routine transactions is healthy, but forced migration of elderly or vulnerable customers is exclusion with regulatory consequences. Footfall decline in a branch predicts its economics two years out. Read with branch cost-to-income (Deep Dive) and assisted-digital support usage.

## Formula

```
Migrated Transactions / Addressable Branch Transactions
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_branch_network_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2117 (batch 6)
