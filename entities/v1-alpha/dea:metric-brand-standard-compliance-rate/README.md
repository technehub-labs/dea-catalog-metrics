# dea:metric-brand-standard-compliance-rate

Candidate Performance Metric record for **Brand Standard Compliance Rate** (BSCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-brand-standard-compliance-rate`
- **Name:** Brand Standard Compliance Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BSCR

## 2. Definition

Brand Standard Compliance Rate (BSCR) measures conformance to standards, plans, or obligations in the Franchise & Multi-site domain. The formula is Audits Meeting Brand Standards / Audits Conducted - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Franchise & multi-site sector.

## 3. Context

Measures the share of locations meeting brand standards in inspections. It matters because brand consistency is the product in multi-site systems. Inspections can drift into announced checklist theater between real audits. Read with Mystery Shopper Score and Customer Satisfaction Score to confirm paper compliance matches customer experience.

## Formula

```
Audits Meeting Brand Standards / Audits Conducted
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** franchise_multi_site
- **Sector:** franchise_multi_site

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 809 (batch 2)
