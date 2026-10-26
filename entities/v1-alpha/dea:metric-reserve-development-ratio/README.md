# dea:metric-reserve-development-ratio

Candidate Performance Metric record for **Reserve Development Ratio** (RDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reserve-development-ratio`
- **Name:** Reserve Development Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RDR

## 2. Definition

Reserve Development Ratio (RDR) addresses exposure to adverse outcomes and is a fixture of actuarial & reserving reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Ultimate Claims / Initially Estimated Claims, expressed in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. Its use is concentrated in Insurance.

## 3. Context

Measures how prior-period reserves have developed against original estimates - adverse or favorable - as reserve adequacy signals emerge over time. Reserve errors are the classic way insurance profit is misstated in both directions, and this ratio reveals which. Distinguish genuine favorable emergence from prior conservatism, and never let one benign year silence multi-year adverse patterns. Read with IBNR accuracy ratio and reserve runoff error rate.

## Formula

```
Ultimate Claims / Initially Estimated Claims
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** actuarial_reserving
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1525 (batch 6)
