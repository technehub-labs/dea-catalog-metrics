# dea:metric-network-segment-compliance

Candidate Performance Metric record for **Network Segment Compliance** (NSGC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-network-segment-compliance`
- **Name:** Network Segment Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NSGC

## 2. Definition

Network Segment Compliance (NSGC) measures conformance to standards, plans, or obligations in the Network Performance & Capacity domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Segments Meeting Zoning Standard / Segments, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures conformance of network segmentation to the approved zone architecture. Segmentation limits lateral movement, the difference between an incident and a breach. Compliance assessed from stale firewall rule sets diverges from runtime reality. Read with cloud network segmentation conformance and mean time to contain - security.

## Formula

```
NSGC = Segments Meeting Zoning Standard / Segments
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3356 (batch 7)
