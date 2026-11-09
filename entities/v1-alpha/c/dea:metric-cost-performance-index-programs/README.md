# dea:metric-cost-performance-index-programs

Candidate Performance Metric record for **Cost Performance Index (Programs)** (CPI-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-performance-index-programs`
- **Name:** Cost Performance Index (Programs)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CPI-P

## 2. Definition

Cost Performance Index (Programs) (CPI-P) captures how efficiently resources are converted into outputs for organizations tracking aerospace & defense program management. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is EV / AC - reported in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Aerospace & Defense sector.

## 3. Context

Measures earned value against actual cost - the efficiency of spend against the baseline. CPI below one on a program is statistically stubborn: the final overrun rarely improves from the point it is measured, which is what makes CPI the single most honest early indicator. Baseline changes reset the index, so annotate rebaselines in trend reading. Read with estimate-at-completion against budget and cost overrun root causes.

## Formula

```
CPI-P = EV / AC
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** aerospace_defense_program_management
- **Sector:** aerospace_defense

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1780 (batch 6)
