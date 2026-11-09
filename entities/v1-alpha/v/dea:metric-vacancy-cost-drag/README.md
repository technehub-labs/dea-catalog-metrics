# dea:metric-vacancy-cost-drag

Candidate Performance Metric record for **Vacancy Cost Drag** (VCD-RE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vacancy-cost-drag`
- **Name:** Vacancy Cost Drag
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** VCD-RE

## 2. Definition

Vacancy Cost Drag (VCD-RE) captures the economic value created or preserved for organizations tracking real estate & mortgage standard measures. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Rent Lost to Vacancy / Potential Gross Rent, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Real estate.

## 3. Context

Measures the cost of unleased space against total potential income. Drag converts vacancy from percentage into P&L pressure. Drag computed only on occupied-potential rent excludes the compounding downtime costs. Read with absorption rate (Market) and economic occupancy rate.

## Formula

```
VCD-RE = Rent Lost to Vacancy / Potential Gross Rent
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** real_estate_mortgage_standard_measures
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4229 (batch 10)
