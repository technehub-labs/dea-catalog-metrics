# dea:metric-product-cannibalization-rate

Candidate Performance Metric record for **Product Cannibalization Rate** (PCR-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-product-cannibalization-rate`
- **Name:** Product Cannibalization Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PCR-T

## 2. Definition

Product Cannibalization Rate (PCR-T) addresses exposure to adverse outcomes and is a fixture of telecom product & bundle management reporting. The formula is Revenue Lost from Existing Products to New Product / Existing Product Baseline - reported in percent (%). It is a standard measure in the Telecommunications sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures the share of new product sales taken from existing products. It matters because net-new growth, not substitution, is what launches must prove. Attribution choices heavily swing the estimate, favoring launch teams when loose. Read with Net Revenue Add from launch and Post-Launch Base Product trends to confirm cannibalization is honestly measured.

## Formula

```
PCR-T = Revenue Lost from Existing Products to New Product / Existing Product Baseline
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecom_product_bundle_management
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1443 (batch 5)
