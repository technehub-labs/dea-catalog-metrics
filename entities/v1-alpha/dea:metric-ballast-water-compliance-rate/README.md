# dea:metric-ballast-water-compliance-rate

Candidate Performance Metric record for **Ballast Water Compliance Rate** (BWCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ballast-water-compliance-rate`
- **Name:** Ballast Water Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BWCR

## 2. Definition

Ballast Water Compliance Rate (BWCR) addresses conformance to standards, plans, or obligations and is a fixture of maritime & shipping reporting. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Ballast Operations Meeting Convention Standards / Operations - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Maritime & shipping sector.

## 3. Context

Measures compliance with ballast water treatment and exchange regulations. It matters because invasive species transfer is a heavily regulated environmental risk with port-state detention consequences. Compliance can be logged on paper while treatment systems malfunction in practice. Read with Port State Inspection findings and treatment system maintenance records to confirm operational compliance.

## Formula

```
BWCR = Ballast Operations Meeting Convention Standards / Operations
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping
- **Sector:** maritime_shipping

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 988 (batch 3)
