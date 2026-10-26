# dea:metric-spill-volume-per-production

Candidate Performance Metric record for **Spill Volume per Production** (SVP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-spill-volume-per-production`
- **Name:** Spill Volume per Production
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SVP

## 2. Definition

Spill Volume per Production (SVP) measures environmental and social sustainability performance in the Oil & Gas domain. It is computed as Hydrocarbons Spilled / Hydrocarbons Produced, expressed in ratio (x:1 or x). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Oil & gas.

## 3. Context

Spill volume per unit of production measures the environmental containment performance of oil and gas operations, normalizing inevitable-seeming loss-of-containment events against operational scale. Volume-weighted measurement matters because the distribution is extreme: a handful of large pipeline events dominate annual totals, so the metric swings on single incidents and year-over-year comparisons mislead without event-level context. The prevention logic differs by failure mode: pipeline spills trace to corrosion management and integrity programs, while tank and valve events trace to inspection discipline. Spill statistics also carry reporting honesty questions about threshold definitions. Read with integrity inspection backlog and remediation timeline, spill containment and recovery effectiveness, and hydrostatic testing program adherence.

## Formula

```
Hydrocarbons Spilled / Hydrocarbons Produced
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** oil_gas
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 890 (batch 3)
