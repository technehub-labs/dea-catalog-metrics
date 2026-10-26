# dea:metric-provision-coverage-ratio

Candidate Performance Metric record for **Provision Coverage Ratio** (PCR-CC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-provision-coverage-ratio`
- **Name:** Provision Coverage Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PCR-CC

## 2. Definition

Provision Coverage Ratio (PCR-CC) measures exposure to adverse outcomes in the Credit & Collections Risk (Enterprise) domain. It is computed as Loan Loss Provision / Non-Performing Exposure, expressed in ratio (x:1 or x). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures loan loss reserves against non-performing or expected losses. Coverage is the balance-sheet honesty check on credit quality. Coverage ratios falling while NPLs rise is the classic pre-crisis signature. Read with expected loss rate (Deep Dive) and allowance for credit losses adequacy.

## Formula

```
PCR-CC = Loan Loss Provision / Non-Performing Exposure
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** credit_collections_risk_enterprise

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4213 (batch 9)
