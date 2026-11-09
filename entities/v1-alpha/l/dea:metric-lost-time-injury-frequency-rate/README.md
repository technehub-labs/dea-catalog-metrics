# dea:metric-lost-time-injury-frequency-rate

Candidate Performance Metric record for **Lost Time Injury Frequency Rate** (LTIFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-lost-time-injury-frequency-rate`
- **Name:** Lost Time Injury Frequency Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LTIFR

## 2. Definition

Lost Time Injury Frequency Rate (LTIFR) addresses exposure to adverse outcomes and is a fixture of health & safety reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as (Lost Time Injuries x 1,000,000) / Total Hours Worked, expressed in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Work injuries causing lost time, normalized per million hours worked - the safety metric that made international comparison possible, standardized under the ILO convention and embedded in every serious safety reporting regime. Its strategic weight is that lost-time injuries are the point where safety becomes undeniably operational: the worker is gone, production is affected, and investigation is mandatory, which removes the gray zone of first-aid classification. The normalization is what makes it useful - per million hours rather than per period - so workforce growth and shrinkage do not distort the trend. Read with the severity companion (lost days rate): an LTIFR improving while severity worsens indicates the mix is shifting toward fewer-but-worse events, which is deterioration wearing an improving metric's clothes.

## Formula

```
LTIFR = (Lost Time Injuries x 1,000,000) / Total Hours Worked
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

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

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 398 (batch 1)
