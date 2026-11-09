# dea:metric-defect-density-deep-dive

Candidate Performance Metric record for **Defect Density (Deep Dive)** (DD-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-defect-density-deep-dive`
- **Name:** Defect Density (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DD-D

## 2. Definition

Defect Density (Deep Dive) (DD-D) captures the quality of outputs and outcomes for organizations tracking semiconductor manufacturing (deep dive). It is computed as Killer Defects per Square Centimetre, expressed in events per thousand or million (scaled). Its use is concentrated in Semiconductors. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures random and systematic defects per unit area on wafers. It is the diagnostic metric of yield engineering: defect density trends link fab process control to die yield outcomes, and kill-ratio weighting (which defects actually destroy devices) separates signal from noise. Density improvements require mechanism-level attribution, not aggregate reduction. Read with die yield (Deep Dive) and inspection sampling coverage.

## Formula

```
DD-D = Killer Defects per Square Centimetre
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** semiconductor_manufacturing_deep_dive
- **Sector:** semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2377 (batch 6)
