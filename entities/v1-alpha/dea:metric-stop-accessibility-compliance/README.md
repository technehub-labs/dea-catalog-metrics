# dea:metric-stop-accessibility-compliance

Candidate Performance Metric record for **Stop Accessibility Compliance** (SAC-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-stop-accessibility-compliance`
- **Name:** Stop Accessibility Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SAC-T

## 2. Definition

Stop Accessibility Compliance (SAC-T) addresses conformance to standards, plans, or obligations and is a fixture of public transit (deep dive) reporting. The formula is Stops Meeting Accessibility Standard / Stops - reported in percent (%). It is a standard measure in the Public Transit sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of stops and stations meeting accessibility standards (ramps, tactile, announcements). Accessibility is both a legal obligation and the transit-equity test: inaccessible stops exclude riders with disabilities from the system entirely, and compliance rates expose how far the network's promise extends in practice. Compliance definitions vary by standard vintage, so annotation matters. Read with accessibility complaint resolution and paratransit demand as the substitute-service signal.

## Formula

```
Stops Meeting Accessibility Standard / Stops
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit_deep_dive
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2419 (batch 6)
