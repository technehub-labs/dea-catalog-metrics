# dea:metric-master-data-completeness-index

Candidate Performance Metric record for **Master Data Completeness Index** (MDCI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-master-data-completeness-index`
- **Name:** Master Data Completeness Index
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MDCI

## 2. Definition

A Master Data Management indicator, Master Data Completeness Index (MDCI) quantifies the quality of outputs and outcomes. It is computed as Composite Completeness of Golden Records, expressed in index (0-100 or normalized). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how completely required attributes are populated across master records. Incomplete records fragment analytics and degrade matching. Completeness measured against permissive schemas (too many optional fields) flatters. Read with critical data element quality index and master data coverage rate.

## Formula

```
Composite Completeness of Golden Records
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** master_data_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3647 (batch 8)
