# dea:metric-farm-to-shelf-traceability-coverage

Candidate Performance Metric record for **Farm-to-Shelf Traceability Coverage** (FSTC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-farm-to-shelf-traceability-coverage`
- **Name:** Farm-to-Shelf Traceability Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FSTC

## 2. Definition

Within Agriculture & Food Processing, Farm-to-Shelf Traceability Coverage (FSTC) is used to gauge conformance to standards, plans, or obligations. It is computed as Batches with Full Traceability Records / Batches, expressed in percent (%). Its use is concentrated in Agriculture & food. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Traceability coverage measures the share of product that can be traced from shelf back to farm through a chain of custody, and it became non-optional as regulators and retailers pushed liability upstream to the grower. The metric's real value is operational, not just compliance: when a contamination event hits, traceability determines whether the recall isolates one grower's Tuesday lot or the entire category for a month. Coverage alone is hollow if not tested - records that exist on paper but fail a mock recall mean nothing under pressure. Read with mock-recall drill time and lot-granularity depth.

## Formula

```
FSTC = Batches with Full Traceability Records / Batches
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agriculture_food_processing
- **Sector:** agriculture_food

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 737 (batch 2)
