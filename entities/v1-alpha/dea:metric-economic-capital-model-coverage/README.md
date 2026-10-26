# dea:metric-economic-capital-model-coverage

Candidate Performance Metric record for **Economic Capital Model Coverage** (ECMC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-economic-capital-model-coverage`
- **Name:** Economic Capital Model Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ECMC

## 2. Definition

Economic Capital Model Coverage (ECMC) captures capability maturity or development for organizations tracking actuarial & reserving. It is computed as Risks Covered by Capital Model / Total Risks, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Insurance.

## 3. Context

Measures the share of material risk types captured within the economic capital model - underwriting, credit, market, operational, catastrophe. Coverage gaps are invisible under-capitalization: risk not modeled is risk priced at zero. Assess whether modeled dependencies and tail scenarios meet supervisory expectations, not just whether risks are named. Read with catastrophe exposure concentration and stress testing outcomes.

## Formula

```
ECMC = Risks Covered by Capital Model / Total Risks
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** actuarial_reserving
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1537 (batch 6)
