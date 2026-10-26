# dea:metric-internal-trust-score

Candidate Performance Metric record for **Internal Trust Score** (ITS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-internal-trust-score`
- **Name:** Internal Trust Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ITS

## 2. Definition

A Culture & Employee Experience indicator, Internal Trust Score (ITS) quantifies the engagement or satisfaction of the people involved. The formula is Average Trust in Leadership Survey Rating - reported in score (points). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures employee confidence in leadership, peers, and organizational processes being fair and truthful. Trust is the hidden multiplier of coordination cost: high trust organizations move fast with thin controls, low trust ones bureaucratize. Self-reported trust is susceptible to mood and recent-events priming, so triangulate with behavioral proxies like escalation volume and information-sharing patterns. Read with psychological safety score and decision cycle time.

## Formula

```
Average Trust in Leadership Survey Rating
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** organization
- **Purpose classification:** engagement
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** culture_employee_experience

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1362 (batch 5)
