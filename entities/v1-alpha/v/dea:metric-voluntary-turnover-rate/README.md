# dea:metric-voluntary-turnover-rate

Candidate Performance Metric record for **Voluntary Turnover Rate** (VTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-voluntary-turnover-rate`
- **Name:** Voluntary Turnover Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** VTR

## 2. Definition

Within Human Resources, Voluntary Turnover Rate (VTR) is used to gauge exposure to adverse outcomes. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Voluntary Departures / Average Headcount - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Employees who chose to leave, as a share of headcount - the component of turnover that carries information, because it separates the people the organization lost from the people it removed. Strategic significance is all in the pattern: regretted versus non-regretted departures, high-performer versus average flight risk, and clustering in particular teams, which almost always indicates a manager problem rather than a market problem. The economic weight is replacement cost - commonly estimated at half to twice annual salary once recruiting, onboarding, and lost productivity are counted - which is why this is a board-level HR metric rather than an administrative one. Benchmark with care: rates above market can reflect a hot talent market rather than dysfunction, and the regretted share is the honest numerator.

## Formula

```
VTR = Voluntary Departures / Average Headcount
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 126 (batch 1)
