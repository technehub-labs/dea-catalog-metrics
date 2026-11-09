# dea:metric-bradford-factor

Candidate Performance Metric record for **Bradford Factor** (BRADF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bradford-factor`
- **Name:** Bradford Factor
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BRADF

## 2. Definition

Within Standard Workforce & Pay Metrics, Bradford Factor (BRADF) is used to gauge exposure to adverse outcomes. It provides the day-to-day signal that a process is running as designed. Its calculation is S^2 x D (Frequency Squared x Days of Absence), measured in score (points). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The Bradford Factor, from Bradford University management practice, scores absence as S squared x D - the frequency of absence spells squared times total days - deliberately weighting frequent short absences harder than one long spell. A score of 100 (say 4 spells of 5 days) is a common informal trigger point; 900 a serious flag. The intent is to distinguish genuine illness (infrequent, longer) from disruptive intermittent absence (frequent, short), which pattern analysis shows harms teams most. It is a conversation trigger, not a punishment formula - use it to start supportive attendance discussions, and beware it can penalize employees with chronic conditions.

## Formula

```
BRADF = S^2 x D (Frequency Squared x Days of Absence)
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** standard_workforce_pay_metrics

## Attribution

- **Source credit:** Bradford University management practice

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4115 (batch 9)
