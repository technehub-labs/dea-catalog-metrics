# dea:metric-days-away-restricted-or-transferred

Candidate Performance Metric record for **Days Away, Restricted, or Transferred** (DART) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-days-away-restricted-or-transferred`
- **Name:** Days Away, Restricted, or Transferred
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DART

## 2. Definition

Days Away, Restricted, or Transferred (DART) addresses exposure to adverse outcomes and is a fixture of health & safety reporting. The formula is (DART Cases x 200,000) / Total Hours Worked - reported in ratio (x:1 or x). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

DART, an OSHA measure, counts injuries per 200,000 hours that resulted in days away, restricted duty, or transfer - capturing both severity and work disruption beyond simple recordables. It matters commercially: DART appears in OSHA recordkeeping, experience modification rates, and many prequalification schemes, and insurers price off it. A gap between TRIR and DART - many recordables but few DART cases - suggests minor injuries dominate; a closing gap suggests escalating severity and warrants intervention.

## Formula

```
DART = (DART Cases x 200,000) / Total Hours Worked
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 399 (batch 1)
