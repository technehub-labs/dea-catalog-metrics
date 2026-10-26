# dea:metric-overall-operations-effectiveness

Candidate Performance Metric record for **Overall Operations Effectiveness** (OOE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-overall-operations-effectiveness`
- **Name:** Overall Operations Effectiveness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OOE

## 2. Definition

Overall Operations Effectiveness (OOE) captures how effectively a process or entity achieves its intended outcome for organizations tracking manufacturing. Its calculation is OEE over Calendar Time Including Planned Stops, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Manufacturing practice.

## 3. Context

The composite of availability, performance, and quality of the constrained operation - the same multiplicative logic as OEE, applied not to a single machine but to the production system as a whole, or as some organizations use it, to the labor-and-asset effectiveness of an entire line or plant. Where OEE diagnoses equipment, OOE diagnoses the operating model: it forces visibility on whether losses come from asset unavailability, running below rate, or making product that fails quality. The multiplicative structure punishes the common pattern of strong component metrics - 90 percent availability times 80 percent performance times 90 percent quality is only 65 percent effective, which is the number that strategies are made from. Its usefulness depends entirely on honest bottleneck identification, since system effectiveness is set by the constraint and improved everywhere else only cosmetically.

## Formula

```
OOE = OEE over Calendar Time Including Planned Stops
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 260 (batch 1)
