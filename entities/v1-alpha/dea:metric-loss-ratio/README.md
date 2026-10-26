# dea:metric-loss-ratio

Candidate Performance Metric record for **Loss Ratio** (LR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-loss-ratio`
- **Name:** Loss Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LR

## 2. Definition

Loss Ratio (LR) measures exposure to adverse outcomes in the Insurance domain. It is computed as Incurred Losses / Earned Premiums, expressed in percent (%). Its use is concentrated in Insurance. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Incurred claims over earned premium - the pure underwriting core of insurance economics, isolating the cost of risk from the cost of running the machine. A ratio around or below the loss ratio assumed in pricing means the actuarial view of the book is correct; above it, either pricing is inadequate, risk selection is deteriorating, or catastrophe has intervened. Strategic use is triage: a company-wide loss ratio blends lines with wildly different norms - property runs high and volatile, specialty liability lower - so movement in the blended number tells you where to look, and movement in a line tells you whether it is a pricing cycle or a reserving problem. Under IFRS 17 the claims side now drags estimates through the discounting machinery, making cross-source comparisons definition-dependent.

## Formula

```
Incurred Losses / Earned Premiums
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 57 (batch 1)
