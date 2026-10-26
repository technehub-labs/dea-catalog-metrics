# dea:metric-absence-rate

Candidate Performance Metric record for **Absence Rate** (AR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-absence-rate`
- **Name:** Absence Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AR

## 2. Definition

Absence Rate (AR) measures the utilization or availability of capacity in the Human Resources domain. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Absent Days / Scheduled Work Days - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures employee absence days as a percentage of scheduled workdays. It matters because unplanned absence is a tax on productivity, coverage, and team morale. It can be under-reported when managers quietly absorb absences without logging them, or inflated by counting approved leave as absence. Read with Overtime Hours and Employee Engagement Score to see whether absence spikes reflect workload or culture problems.

## Formula

```
Absent Days / Scheduled Work Days
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 131 (batch 1)
