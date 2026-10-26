# dea:metric-regulatory-inspection-observations

Candidate Performance Metric record for **Regulatory Inspection Observations** (RIO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regulatory-inspection-observations`
- **Name:** Regulatory Inspection Observations
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RIO

## 2. Definition

Regulatory Inspection Observations (RIO) addresses conformance to standards, plans, or obligations and is a fixture of pharmaceuticals & life sciences reporting. The formula is Observations from Regulatory Inspections - reported in count (items per period). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Pharmaceuticals sector.

## 3. Context

Findings issued by agency inspectors - the metric where manufacturing compliance becomes concrete, since the observation categories (critical, major, minor) and their trend are the primary evidence regulators and markets use to judge a site's control state. Its strategic weight is consequence: critical observations drive warning letters, consent decrees, and import alerts, any of which can remove a revenue-generating site from supply at a stroke - which is why inspection-readiness programs treat trend in observations as a board-level risk signal. The honest analysis is by system: observations clustered in one quality system (deviation management, data integrity, environmental monitoring) indicate a structural weakness worth a remediation program, while scattered minor findings indicate drift rather than failure. The pair that matters most in recent enforcement practice is data integrity - where a single finding pattern (deleted records, shared passwords) can invalidate years of testing data across products.

## Formula

```
Observations from Regulatory Inspections
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** pharmaceuticals_life_sciences
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 485 (batch 1)
