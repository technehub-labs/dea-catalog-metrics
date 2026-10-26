# dea:metric-best-possible-dso-gap

Candidate Performance Metric record for **Best Possible DSO Gap** (BPDG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-best-possible-dso-gap`
- **Name:** Best Possible DSO Gap
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BPDG

## 2. Definition

Within Accounts Payable & Receivable Operations (Deep Dive), Best Possible DSO Gap (BPDG) is used to gauge how efficiently resources are converted into outputs. The formula is DSO minus Best Possible DSO - reported in days. It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the gap between actual DSO and the theoretical minimum given payment terms. The gap isolates collection-process friction from contractual reality. Best-possible models that ignore billing delays understate the gap. Read with days sales outstanding (Deep Dive) and dispute resolution cycle time.

## Formula

```
BPDG = DSO minus Best Possible DSO
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** accounts_payable_receivable_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3803 (batch 8)
