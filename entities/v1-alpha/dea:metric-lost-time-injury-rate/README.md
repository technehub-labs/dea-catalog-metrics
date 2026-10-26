# dea:metric-lost-time-injury-rate

Candidate Performance Metric record for **Lost Time Injury Rate** (LTIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-lost-time-injury-rate`
- **Name:** Lost Time Injury Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LTIR

## 2. Definition

Lost Time Injury Rate (LTIR) captures exposure to adverse outcomes for organizations tracking health & safety. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as (Lost Time Injuries x 200,000) / Total Hours Worked, expressed in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

LTIF counts lost-time injuries per million hours worked (per 200,000 hours in some conventions) - the most widely used international lagging safety metric. Unlike TRIR it captures only injuries serious enough to keep someone off work, making it a better proxy for severity, though definitions of lost time vary by jurisdiction. Boards typically expect a steady multi-year downtrend; a flat or rising LTIF usually triggers a safety-culture review rather than a policy tweak.

## Formula

```
(Lost Time Injuries x 200,000) / Total Hours Worked
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

- **Source credit:** OSHA / ILO convention

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 397 (batch 1)
