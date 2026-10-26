# dea:metric-fuel-burn-per-block-hour-deep-dive

Candidate Performance Metric record for **Fuel Burn per Block Hour (Deep Dive)** (FPBH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fuel-burn-per-block-hour-deep-dive`
- **Name:** Fuel Burn per Block Hour (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FPBH

## 2. Definition

Fuel Burn per Block Hour (Deep Dive) (FPBH) addresses how efficiently resources are converted into outputs and is a fixture of airline & transportation standard measures (deep dive) reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Fuel Consumed / Block Hours, expressed in currency per unit. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Airlines & Aviation.

## 3. Context

Measures fuel consumption per aircraft operating hour. Fuel is the largest volatile cost in aviation. Burn improved by heavier stage-skipping maintenance is cost relocation. Read with cost per available seat kilometer and fuel hedging effectiveness.

## Formula

```
Fuel Consumed / Block Hours
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** operations
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** airline_transportation_standard_measures_deep_dive
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4293 (batch 10)
