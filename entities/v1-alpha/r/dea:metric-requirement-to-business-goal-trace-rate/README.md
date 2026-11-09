# dea:metric-requirement-to-business-goal-trace-rate

Candidate Performance Metric record for **Requirement-to-Business-Goal Trace Rate** (RBGT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-requirement-to-business-goal-trace-rate`
- **Name:** Requirement-to-Business-Goal Trace Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RBGT

## 2. Definition

Requirement-to-Business-Goal Trace Rate (RBGT) captures the economic value created or preserved for organizations tracking requirements engineering & product discovery. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Requirements Linked to Business Goals / Requirements - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of requirements linked to business goals or user outcomes. It is the anti-waste control of requirements engineering: untraced requirements are how features without value enter roadmaps, and trace rate makes scope-review conversations evidence-based. Trace links must be honest (decorative linkage to satisfy process is common), so sample-audit the chains. Read with product discovery-to-delivery ratio (Deep Dive) and outcome measurement of shipped features.

## Formula

```
RBGT = Requirements Linked to Business Goals / Requirements
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** requirements_engineering_product_discovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2611 (batch 7)
