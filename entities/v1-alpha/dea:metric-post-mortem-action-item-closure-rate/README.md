# dea:metric-post-mortem-action-item-closure-rate

Candidate Performance Metric record for **Post-Mortem Action Item Closure Rate** (PMAICR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-post-mortem-action-item-closure-rate`
- **Name:** Post-Mortem Action Item Closure Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PMAICR

## 2. Definition

A SecOps & Security Operations Center indicator, Post-Mortem Action Item Closure Rate (PMAICR) quantifies conformance to standards, plans, or obligations. The formula is Security Action Items Closed by Target / Items - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of corrective actions from security post-mortems completed by their due dates. Unclosed action items are lessons acknowledged but not learned. Closure rates can be inflated by closing easy items while systemic fixes stall. Read with incident post-mortem completion rate and security incident recurrence rate.

## Formula

```
Security Action Items Closed by Target / Items
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2785 (batch 7)
