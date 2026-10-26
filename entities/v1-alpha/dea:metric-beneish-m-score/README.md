# dea:metric-beneish-m-score

Candidate Performance Metric record for **Beneish M-Score** (BENM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-beneish-m-score`
- **Name:** Beneish M-Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BENM

## 2. Definition

A Valuation & Corporate Finance Standard Measures indicator, Beneish M-Score (BENM) quantifies exposure to adverse outcomes. It is computed as Composite of Eight Manipulation-Signal Ratios, expressed in score (points). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

The Beneish M-Score, from Messod D. Beneish (1999), is a weighted composite of eight ratios (DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA) built to detect earnings manipulation. A score above -1.78 (i.e., less negative) flags a firm as a likely manipulator - in Beneish's sample it flagged Enron pre-collapse. It is a screening probability, not proof: high growth legitimately moves some of the inputs. Use it as a red-flag review trigger alongside accrual analysis and segment consistency checks.

## Formula

```
Composite of Eight Manipulation-Signal Ratios
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** valuation_corporate_finance_standard_measures

## Attribution

- **Source credit:** Messod D. Beneish, 1999

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4037 (batch 9)
