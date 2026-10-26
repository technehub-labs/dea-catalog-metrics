# dea:metric-deal-win-rate-mandated

Candidate Performance Metric record for **Deal Win Rate (Mandated)** (DWR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deal-win-rate-mandated`
- **Name:** Deal Win Rate (Mandated)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DWR

## 2. Definition

Deal Win Rate (Mandated) (DWR) captures how effectively a process or entity achieves its intended outcome for organizations tracking investment banking & capital markets. Its calculation is Mandates Won / Mandates Pitched, measured in percent (%). It originates from and is most used in Investment banking practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Deal win rate (mandated) measures the share of formal pitch processes converted into mandates, and it is the sales-effectiveness metric of investment banking - banking is a pitch business, and the ratio of pitch effort to mandate flow determines whether the senior-banker time investment pays. The decomposition is the diagnostic: win rate by deal type, by client tier (incumbent relationships win more than cold pitches), and by competitor set each carry different meaning, and loss reasons (fee, team, brand, product depth) point at the fixable drivers. The strategic subtlety is pitch selectivity: high win rates can mean only pitching sure things, so win rate should be read with pitch volume and mandate revenue. Read with revenue per pitch (the full-funnel metric), incumbent versus new-client win split, and loss-reason trend.

## Formula

```
Mandates Won / Mandates Pitched
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_banking_capital_markets
- **Sector:** investment_banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1146 (batch 4)
