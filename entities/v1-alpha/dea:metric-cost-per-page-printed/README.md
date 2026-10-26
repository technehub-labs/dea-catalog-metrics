# dea:metric-cost-per-page-printed

Candidate Performance Metric record for **Cost per Page Printed** (CPP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-page-printed`
- **Name:** Cost per Page Printed
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CPP

## 2. Definition

Cost per Page Printed (CPP) addresses how efficiently resources are converted into outputs and is a fixture of printing & publishing reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Total Production Cost / Pages Printed, measured in currency per unit. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Printing & publishing practice.

## 3. Context

Measures total cost per page across production printing. It matters because per-page economics decide competitiveness in commoditized print. Costs can be cut by deferring press maintenance that degrades quality later. Read with Rework Rate and Equipment Utilization to confirm unit cost gains are structural.

## Formula

```
Total Production Cost / Pages Printed
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** printing_publishing
- **Sector:** printing_publishing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1263 (batch 4)
