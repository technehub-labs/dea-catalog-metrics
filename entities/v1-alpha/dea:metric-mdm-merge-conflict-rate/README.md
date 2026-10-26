# dea:metric-mdm-merge-conflict-rate

Candidate Performance Metric record for **MDM Merge Conflict Rate** (MDCR-MD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mdm-merge-conflict-rate`
- **Name:** MDM Merge Conflict Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MDCR-MD

## 2. Definition

MDM Merge Conflict Rate (MDCR-MD) captures the quality of outputs and outcomes for organizations tracking master data management. It is defined as Manual Merge Interventions / Merge Attempts; the result is stated in percent (%). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
MDCR-MD = Manual Merge Interventions / Merge Attempts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** master_data_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3642 (batch 8)
