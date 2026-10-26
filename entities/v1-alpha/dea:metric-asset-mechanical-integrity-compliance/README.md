# dea:metric-asset-mechanical-integrity-compliance

Candidate Performance Metric record for **Asset Mechanical Integrity Compliance** (AMIC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-asset-mechanical-integrity-compliance`
- **Name:** Asset Mechanical Integrity Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AMIC

## 2. Definition

Asset Mechanical Integrity Compliance (AMIC) addresses conformance to standards, plans, or obligations and is a fixture of oil & gas downstream & refining reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Inspections within Integrity Window / Due - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Oil & Gas sector.

## 3. Context

Measures completion of inspection and maintenance schedules for pressure vessels, piping, and rotating equipment. Mechanical integrity is the process-safety foundation of refining, and deferral is the mechanism by which catastrophic events get scheduled - integrity programs cut first in downturns, with consequences arriving years later. Compliance by risk-based priority beats simple completion counts. Read with corrosion-circuit inspection findings and SIS test compliance.

## Formula

```
Inspections within Integrity Window / Due
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** oil_gas_downstream_refining
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2308 (batch 6)
