# dea:metric-vault-reconciliation-error-rate

Candidate Performance Metric record for **Vault Reconciliation Error Rate** (VRER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vault-reconciliation-error-rate`
- **Name:** Vault Reconciliation Error Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VRER

## 2. Definition

Vault Reconciliation Error Rate (VRER) captures the quality of outputs and outcomes for organizations tracking retail banking branch network (deep dive). The formula is Vault Reconciliation Discrepancies / Reconciliations - reported in events per thousand or million (scaled). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Banking sector.

## Formula

```
Vault Reconciliation Discrepancies / Reconciliations
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_branch_network_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2123 (batch 6)
