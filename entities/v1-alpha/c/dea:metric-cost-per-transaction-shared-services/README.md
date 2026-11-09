# dea:metric-cost-per-transaction-shared-services

Candidate Performance Metric record for **Cost per Transaction (Shared Services)** (CPT-G) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-transaction-shared-services`
- **Name:** Cost per Transaction (Shared Services)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CPT-G

## 2. Definition

Cost per Transaction (Shared Services) (CPT-G) addresses how efficiently resources are converted into outputs and is a fixture of shared services & global business services reporting. It is defined as Total Service Cost / Transactions Processed; the result is stated in currency per unit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Cost per transaction in shared services measures the fully loaded unit cost of a processed transaction - invoice processed, ticket resolved, payment run - and it is the founding promise metric of the shared-services model: consolidating fragmented back-office work into scaled operations should drive unit costs down through volume, standardization, and automation. The metric's honest reading requires price-adjustment discipline: shared-services cost is an internal chargeback, so inflation of the internal rate is invisible to the business unless benchmarks hold it accountable externally. Scope-mix drift distorts comparisons - a services center absorbing complex new work types will show rising cost per transaction despite improving efficiency. Read with automation-rate trend (cost reduction should trace to it), external benchmark positioning by function, and service-level achievement to catch cost reduction purchased with service degradation.

## Formula

```
CPT-G = Total Service Cost / Transactions Processed
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** shared_services_global_business_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1054 (batch 4)
