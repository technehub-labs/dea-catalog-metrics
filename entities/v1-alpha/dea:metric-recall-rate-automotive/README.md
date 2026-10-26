# dea:metric-recall-rate-automotive

Candidate Performance Metric record for **Recall Rate (Automotive)** (RRA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recall-rate-automotive`
- **Name:** Recall Rate (Automotive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RRA

## 2. Definition

Recall Rate (Automotive) (RRA) addresses exposure to adverse outcomes and is a fixture of automotive reporting. Its calculation is Recalled Vehicles / Vehicles Sold, measured in percent (%). It originates from and is most used in Automotive practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Recall rate measures vehicles recalled per vehicles sold (or recalls per model per period), and it is the industry's scarlet letter - each large recall generates headlines, dealer burden, and regulatory scrutiny that outlasts the direct cost. The rise of over-the-air fixes has begun splitting this metric: software recalls patched remotely are a different order of severity than physical ones requiring dealer visits. Watch for the OEM-versus-supplier allocation question, since much depends on how blame and cost are contractually distributed. Read alongside NHTSA defect investigation counts and field failure rate telemetry for earlier signals.

## Formula

```
Recalled Vehicles / Vehicles Sold
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 748 (batch 2)
