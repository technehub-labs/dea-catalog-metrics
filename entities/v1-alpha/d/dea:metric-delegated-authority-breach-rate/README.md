# dea:metric-delegated-authority-breach-rate

Candidate Performance Metric record for **Delegated Authority Breach Rate** (DABR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-delegated-authority-breach-rate`
- **Name:** Delegated Authority Breach Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DABR

## 2. Definition

Delegated Authority Breach Rate (DABR) captures conformance to standards, plans, or obligations for organizations tracking regulatory affairs & compliance operations. Its calculation is Decisions beyond Delegated Limits / Decisions Sampled, measured in events per thousand or million (scaled). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
DABR = Decisions beyond Delegated Limits / Decisions Sampled
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** regulatory_affairs_compliance_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1604 (batch 6)
