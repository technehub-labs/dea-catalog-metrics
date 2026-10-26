# dea:metric-coupling-index

Candidate Performance Metric record for **Coupling Index** (COUI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-coupling-index`
- **Name:** Coupling Index
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** COUI

## 2. Definition

Coupling Index (COUI) addresses the quality of outputs and outcomes and is a fixture of software architecture & technical design reporting. The formula is Cross-Module Dependencies per Module - reported in ratio (x:1 or x). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures interdependencies between modules or services. Coupling is the change-velocity governor of software systems: tightly coupled code changes together, breaks together, and slows teams into coordination gridlock, and the index quantifies that drag. Static analysis gives structural coupling, but semantic coupling (hidden runtime assumptions) is the more dangerous kind and needs design review. Read with deployment independence of services and change-failure correlation across coupled components.

## Formula

```
Cross-Module Dependencies per Module
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_architecture_technical_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2621 (batch 7)
