# dea:metric-expected-loss-rate-deep-dive

Candidate Performance Metric record for **Expected Loss Rate (Deep Dive)** (ELRDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-expected-loss-rate-deep-dive`
- **Name:** Expected Loss Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ELRDD

## 2. Definition

Expected Loss Rate (Deep Dive) (ELRDD) captures exposure to adverse outcomes for organizations tracking credit & collections risk (enterprise). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as PD x LGD x EAD / Portfolio Exposure, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures PD times LGD times EAD, the risk-priced cost of the portfolio. EL is the number that should price credit and set reserves. Model outputs lag realized losses, so backtesting matters. Read with provision coverage ratio and credit loss rate (portfolio).

## Formula

```
ELRDD = PD x LGD x EAD / Portfolio Exposure
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** credit_collections_risk_enterprise

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4198 (batch 9)
