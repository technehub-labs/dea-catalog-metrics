# dea:metric-global-process-standardization-rate

Candidate Performance Metric record for **Global Process Standardization Rate** (GPSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-global-process-standardization-rate`
- **Name:** Global Process Standardization Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GPSR

## 2. Definition

Global Process Standardization Rate (GPSR) captures capability maturity or development for organizations tracking shared services & global business services. The formula is Entities Using Standard Process / Total Entities Served - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Global process standardization rate measures the share of processes that follow a single global design versus local variants, and it is the scalability-infrastructure metric of global business services - the entire GBS value proposition (one process design, one system, one capability team, deployed worldwide) collapses if every country keeps its variant. The strategic trade-off is real and must be priced: local processes often encode local regulatory requirements (e.g., statutory reporting, tax formats) or genuine business differences, and forced standardization that ignores legitimate variation produces compliance failures. The honest measurement distinguishes mandated-variation (regulatory) from voluntary-variation (local preference), targeting standardization only where the second is the driver. Read with variance-cause analysis for non-standard processes, process design governance (who can approve a deviation), and the cost differential between standard and variant processes.

## Formula

```
GPSR = Entities Using Standard Process / Total Entities Served
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** shared_services_global_business_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1059 (batch 4)
