# dea:metric-supplier-quality-rating

Candidate Performance Metric record for **Supplier Quality Rating** (SQR-Q) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supplier-quality-rating`
- **Name:** Supplier Quality Rating
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SQR-Q

## 2. Definition

Supplier Quality Rating (SQR-Q) addresses the quality of outputs and outcomes and is a fixture of quality management reporting. It is computed as Accepted Lots / Total Lots Received, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures a composite quality score for suppliers, blending defect, escape, and responsiveness data. It matters because it directs sourcing away from suppliers who quietly cost more in failure. Composite scores can obscure single catastrophic signals behind good averages. Read with Supplier Defect Rate and Audit Nonconformance findings to inspect the components before trusting the composite.

## Formula

```
SQR-Q = Accepted Lots / Total Lots Received
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 242 (batch 1)
