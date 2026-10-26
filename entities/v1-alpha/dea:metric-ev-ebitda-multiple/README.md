# dea:metric-ev-ebitda-multiple

Candidate Performance Metric record for **EV/EBITDA Multiple** (EVEBITDA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ev-ebitda-multiple`
- **Name:** EV/EBITDA Multiple
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EVEBITDA

## 2. Definition

Within Valuation & Corporate Finance Standard Measures, EV/EBITDA Multiple (EVEBITDA) is used to gauge the economic value created or preserved. Its calculation is Enterprise Value / EBITDA, measured in ratio (x:1 or x). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures enterprise value relative to EBITDA. It is the standard cross-capital-structure valuation comparator. Multiples are sector-cyclical: cheap can mean deteriorating. Read with earnings yield (Deep Dive) and peer valuation multiple comparison.

## Formula

```
Enterprise Value / EBITDA
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** valuation_corporate_finance_standard_measures

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4043 (batch 9)
