# dea:metric-shadow-vendor-count

Candidate Performance Metric record for **Shadow Vendor Count** (SVC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-shadow-vendor-count`
- **Name:** Shadow Vendor Count
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SVC

## 2. Definition

A Outsourcing & Vendor Management indicator, Shadow Vendor Count (SVC) quantifies conformance to standards, plans, or obligations. The formula is Unapproved Vendors with Spend in Period - reported in count (items per period). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures undocumented or unmanaged vendors operating outside procurement control. It matters because shadow vendors bypass security, legal, and financial controls entirely. Discovery is imperfect, so a stable low count can mean blindness, not control. Read with Maverick Spend Rate and vendor risk assessment coverage to confirm the count reflects real visibility.

## Formula

```
Unapproved Vendors with Spend in Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** outsourcing_vendor_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1132 (batch 4)
