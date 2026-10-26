# dea:metric-scope-2-emissions-intensity

Candidate Performance Metric record for **Scope 2 Emissions Intensity** (S2EI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-scope-2-emissions-intensity`
- **Name:** Scope 2 Emissions Intensity
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** S2EI

## 2. Definition

Scope 2 Emissions Intensity (S2EI) measures environmental and social sustainability performance in the Environmental, Social & Governance Reporting domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Scope 2 tCO2e / Revenue Unit, measured in tonnes CO2 equivalent (tCO2e). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures purchased-energy emissions, market- or location-based, per output. Scope 2 is the most tractable emissions category - procurement decisions (renewable PPAs, supplier switching) move it directly - which is why it is usually the first reduction target. Market-based accounting of unbundled certificates is the honesty question, since paper reductions without physical change invite scrutiny. Read with renewable electricity share and contractual-instrument quality.

## Formula

```
Scope 2 tCO2e / Revenue Unit
```

## Unit

- **Unit reference:** `dea:unit-tonne`
- **Unit:** tonne
- **Unit label (as published):** tonnes CO2 equivalent (tCO2e)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** sustainability
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** environmental_social_governance_reporting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2194 (batch 6)
