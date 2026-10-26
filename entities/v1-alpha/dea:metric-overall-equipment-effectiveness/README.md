# dea:metric-overall-equipment-effectiveness

Candidate Performance Metric record for **Overall Equipment Effectiveness** (OEE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-overall-equipment-effectiveness`
- **Name:** Overall Equipment Effectiveness
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OEE

## 2. Definition

Within Operations, Overall Equipment Effectiveness (OEE) is used to gauge how effectively a process or entity achieves its intended outcome. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Availability x Performance x Quality, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

OEE multiplies three loss factors - Availability (did the machine run?), Performance (at rated speed?), Quality (good output?) - into one figure for how much planned production time was truly productive. Rooted in Seiichi Nakajima's TPM tradition (1980s), a perfect OEE is 100%, 85% is conventionally world-class, and most plants run far below it - often without knowing, because each loss is tracked in a different silo. Its power is decomposition: an OEE of 60% could stem from chronic breakdowns, micro-stops, or slow cycles, and the factor breakdown tells you which. Measure it per machine at constraint assets, where lost time is lost revenue; fleet-wide averages blur the signal.

## Formula

```
Availability x Performance x Quality
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Seiichi Nakajima (TPM tradition), 1980s

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 152 (batch 1)
