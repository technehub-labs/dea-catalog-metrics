# dea:metric-staff-leverage-ratio

Candidate Performance Metric record for **Staff Leverage Ratio** (SLR-PS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-staff-leverage-ratio`
- **Name:** Staff Leverage Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SLR-PS

## 2. Definition

Staff Leverage Ratio (SLR-PS) measures the utilization or availability of capacity in the Professional Services domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Non-Partner Staff / Partners; the result is stated in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. In Professional services, it is a recognized element of the standard performance toolkit.

## 3. Context

The ratio of junior delivery staff to senior (partner-level) staff - the structural metric of the professional-services model, and the one that encodes the entire economics: partners sell and supervise, juniors deliver, and the margin comes from the spread between blended delivery cost and billing rates times how many juniors each partner can productively supervise. Its strategic significance is the scale test: high leverage produces high margin per partner in routine work, low leverage produces premium pricing in expert work, and the right ratio depends entirely on the service being sold - the classic strategic distinction between volume and expertise models. Read with utilization and realization by level, since leverage only pays when the junior hours are billable and the quality holds: an over-leveraged pyramid shows up as quality failures and partner time consumed by rework, the pattern that converts leverage from profit engine to liability. The trend matters most: pyramids that flatten over time are usually the senior-rank aging of the firm wearing a structural change's clothes.

## Formula

```
Non-Partner Staff / Partners
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** professional_services
- **Sector:** professional_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 684 (batch 2)
