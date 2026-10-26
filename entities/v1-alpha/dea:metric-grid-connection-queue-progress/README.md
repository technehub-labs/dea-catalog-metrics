# dea:metric-grid-connection-queue-progress

Candidate Performance Metric record for **Grid Connection Queue Progress** (GCQP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-grid-connection-queue-progress`
- **Name:** Grid Connection Queue Progress
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GCQP

## 2. Definition

Grid Connection Queue Progress (GCQP) addresses the utilization or availability of capacity and is a fixture of energy transition & renewables reporting. It is defined as Projects with Executed Grid Agreement / Projects in Queue; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Renewable energy, it is a recognized element of the standard performance toolkit.

## 3. Context

Grid connection queue progress measures advancement through the interconnection process - the application, study, agreement, and construction phases required to connect generation to the transmission grid - and it is the binding-constraint metric of the renewables buildout: interconnection queues have grown to the point where projects routinely wait years, and a substantial share of queued capacity never gets built, making queue position a project-value determinant. The queue's structure matters: the process is sequential and trigger-cascading (each study phase feeds the next), and withdrawal-and-replacement dynamics mean published queue totals overstate realistic pipeline. The commercial signal is optionality value: a project with an executed interconnection agreement carries value independent of its generation economics, since it holds a grid access right others cannot get. Read with study-completion milestones, commercial-operation-date commitment realism, and the queue-withdrawal rate as the conversion signal.

## Formula

```
Projects with Executed Grid Agreement / Projects in Queue
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_transition_renewables
- **Sector:** renewable_energy

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1110 (batch 4)
