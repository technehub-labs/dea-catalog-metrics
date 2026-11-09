# dea:metric-total-recordable-incident-rate

Candidate Performance Metric record for **Total Recordable Incident Rate** (TRIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-total-recordable-incident-rate`
- **Name:** Total Recordable Incident Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TRIR

## 2. Definition

Within Health & Safety, Total Recordable Incident Rate (TRIR) is used to gauge exposure to adverse outcomes. Its calculation is (Recordable Injuries x 200,000) / Total Hours Worked, measured in ratio (x:1 or x). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

TRIR, defined by OSHA, is the number of recordable injuries and illnesses per 200,000 hours worked - effectively per 100 full-time workers per year. It is the headline safety statistic in US regulatory reporting and contractor qualification: a TRIR of 1.0 means one recordable incident per 100 FTE-years, and many clients disqualify vendors above 2-3. Its weakness is that low incident counts make it statistically noisy for small sites, and it can incentivize under-reporting; pair it with leading indicators (near misses, audits) for a fair picture.

## Formula

```
TRIR = (Recordable Injuries x 200,000) / Total Hours Worked
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** health_safety

## Attribution

- **Source credit:** OSHA (US Dept. of Labor)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 396 (batch 1)
