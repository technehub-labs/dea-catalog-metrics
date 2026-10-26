# dea:metric-technology-currency-index

Candidate Performance Metric record for **Technology Currency Index** (TCI-SA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-technology-currency-index`
- **Name:** Technology Currency Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TCI-SA

## 2. Definition

Technology Currency Index (TCI-SA) addresses exposure to adverse outcomes and is a fixture of software architecture & technical design reporting. The formula is Components on Supported Versions / Components - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of the stack on current, supported versions of frameworks, runtimes, and platforms. Currency is the compound-interest metric of software maintenance: every outdated component accumulates security exposure, upgrade friction, and incompatibility until migration becomes a crisis project. Index construction should weight by criticality and support-expiry proximity. Read with technical debt ratio (Deep Dive) and vulnerability remediation timelines.

## Formula

```
TCI-SA = Components on Supported Versions / Components
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_architecture_technical_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2639 (batch 7)
