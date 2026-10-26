# dea:metric-employee-engagement-score

Candidate Performance Metric record for **Employee Engagement Score** (EES) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-employee-engagement-score`
- **Name:** Employee Engagement Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EES

## 2. Definition

A Human Resources indicator, Employee Engagement Score (EES) quantifies the engagement or satisfaction of the people involved. The formula is Weighted Index of Engagement Survey Items - reported in score (points). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

A composite index from survey instruments measuring commitment, advocacy, and discretionary effort - the metric that made the Gallup Q12 famous and moved engagement from an HR program to a business performance predictor. The research tradition behind it claims correlations between top-quartile engagement and profitability, productivity, and quality outcomes that no other HR measure approaches, which is why executives review it quarterly in mature organizations. Its strategic power is at team level: engagement varies more between teams in the same company than between companies, so the unit of action is the manager, not the enterprise. The failure mode is survey fatigue and gaming - response rates falling below 70 percent, or scores rising after visible consequences attach to them, both of which convert the metric into theater.

## Formula

```
Weighted Index of Engagement Survey Items
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
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 129 (batch 1)
