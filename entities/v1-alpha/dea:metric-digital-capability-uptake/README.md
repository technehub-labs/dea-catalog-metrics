# dea:metric-digital-capability-uptake

Candidate Performance Metric record for **Digital Capability Uptake** (DCU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-digital-capability-uptake`
- **Name:** Digital Capability Uptake
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DCU

## 2. Definition

Within Digital Transformation, Digital Capability Uptake (DCU) is used to gauge how effectively a process or entity achieves its intended outcome. It is computed as Users Adopting New Digital Capability / Target Users, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures adoption of new digital capabilities across the transformation portfolio. It matters because unused capability is transformation spend without benefit. Uptake can be counted at license or deployment level rather than active use. Read with Feature Usage Rate and Benefit Realization against the business case to confirm uptake creates value.

## Formula

```
DCU = Users Adopting New Digital Capability / Target Users
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** effectiveness
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** digital_transformation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1313 (batch 5)
