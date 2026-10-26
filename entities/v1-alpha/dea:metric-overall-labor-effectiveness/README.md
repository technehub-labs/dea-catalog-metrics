# dea:metric-overall-labor-effectiveness

Candidate Performance Metric record for **Overall Labor Effectiveness** (OLE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-overall-labor-effectiveness`
- **Name:** Overall Labor Effectiveness
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OLE

## 2. Definition

Overall Labor Effectiveness (OLE) addresses how effectively a process or entity achieves its intended outcome and is a fixture of operations reporting. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Availability x Performance x Quality of Direct Labor - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the compound of labor availability, performance, and quality in production operations. It matters because it isolates how much paid labor actually becomes good output. Component definitions are flexible, so gaming means scoring each element generously rather than fixing losses. Read with Labor Productivity and Absenteeism trends to locate whether losses come from absence, pace, or quality.

## Formula

```
Availability x Performance x Quality of Direct Labor
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** effectiveness
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 171 (batch 1)
