# dea:metric-vendor-risk-assessment-currency

Candidate Performance Metric record for **Vendor Risk Assessment Currency** (VRAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vendor-risk-assessment-currency`
- **Name:** Vendor Risk Assessment Currency
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VRAC

## 2. Definition

Vendor Risk Assessment Currency (VRAC) captures conformance to standards, plans, or obligations for organizations tracking outsourcing & vendor management. It is computed as Vendors with Assessment within Review Cycle / Critical Vendors, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Vendor risk assessment currency measures the share of vendor relationships with current, complete risk assessments (security posture, financial stability, compliance status, concentration exposure), and it is the due-diligence infrastructure metric of third-party risk management - the regulatory expectation (and contractual reality in many regulated industries) is that critical vendors are assessed before engagement and re-assessed on risk-appropriate cycles. The honesty issue is assessment depth: a questionnaire returned by the vendor (self-attested) is worth far less than an independent assessment (SOC 2 reports, penetration-test evidence, financial statements), so currency metrics that treat both as equal flatter the state of coverage. Concentration matters as much as currency: a vendor that has become critical since its last assessment carries risk the cadence cannot see. Read with assessment-recency distribution by criticality tier, overdue-assessment aging, and exception-approval volume for late assessments.

## Formula

```
Vendors with Assessment within Review Cycle / Critical Vendors
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
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** outsourcing_vendor_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1125 (batch 4)
