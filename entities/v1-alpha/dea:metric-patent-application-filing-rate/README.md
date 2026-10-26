# dea:metric-patent-application-filing-rate

Candidate Performance Metric record for **Patent Application Filing Rate** (PAFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-patent-application-filing-rate`
- **Name:** Patent Application Filing Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PAFR

## 2. Definition

Patent Application Filing Rate (PAFR) captures growth over time for organizations tracking r&d and innovation. The formula is Patent Applications Filed per Period - reported in count (items per period). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Patent applications filed per period, often normalized per R&D dollar or per researcher - the activity metric of the IP generation process, carrying strategic weight through what filing volume achieves: defensive coverage, freedom-to-operate, licensing positions, and the optionality of future grants. Its significance is the leading-indicator role: applications precede products by years, so filing-rate trends in a technology class signal where firms are investing their futures, and patent-analytics practice reads competitor filings precisely for that reason. The honest read is quality-weighted: application counts reward broad filing programs over selective ones, and jurisdictions differ in examination rigor such that family size (the number of jurisdictions an invention is filed in) is the better proxy for how much the applicant values the invention. Read with the grant rate, which tells whether the activity is producing assets.

## Formula

```
Patent Applications Filed per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** r_d_and_innovation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 539 (batch 1)
