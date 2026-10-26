# dea:metric-case-processing-time

Candidate Performance Metric record for **Case Processing Time** (CPT-G) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-case-processing-time`
- **Name:** Case Processing Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPT-G

## 2. Definition

Case Processing Time (CPT-G) addresses how efficiently resources are converted into outputs and is a fixture of public sector & government reporting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Days from Case Receipt to Case Closure, expressed in days. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Public sector.

## 3. Context

Measures average time to complete a citizen or administrative case. It matters because processing delays are the most citizen-visible government performance failure. It can be gamed by closing easy cases first while complex ones age, or by reclassifying stalled cases as pending information. Read with Backlog of Pending Cases and First-Time Resolution of Citizen Requests to confirm speed is real across the whole docket.

## Formula

```
Days from Case Receipt to Case Closure
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** public_sector_government
- **Sector:** public_sector

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 635 (batch 2)
