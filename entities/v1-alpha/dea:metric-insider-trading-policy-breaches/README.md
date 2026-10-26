# dea:metric-insider-trading-policy-breaches

Candidate Performance Metric record for **Insider Trading Policy Breaches** (ITPB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-insider-trading-policy-breaches`
- **Name:** Insider Trading Policy Breaches
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ITPB

## 2. Definition

Insider Trading Policy Breaches (ITPB) addresses exposure to adverse outcomes and is a fixture of corporate governance reporting. It is defined as Detected Insider Dealing Breaches per Period; the result is stated in count (items per period). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Insider trading policy breaches count violations of the company's insider trading compliance framework - blackout windows, pre-clearance requirements, trading restrictions for insiders with material non-public information, and they are the legal-exposure metric of equity-market integrity. The stakes are severe: insider trading is a securities-fraud offense with civil and criminal consequences, and the company itself faces liability for failure to maintain controls if its insiders trade. The metric's structure is near-zero-tolerance: one material breach matters more than any rate, which makes trend-line analysis less useful than case review. The honest measurement includes detection effectiveness - breaches surfaced by self-audit versus by regulator both count, but the second signals control failure. Read with blackout-window compliance rates, pre-clearance rejection and override patterns, Section 16 filing timeliness (its adjacent compliance obligation), and training completion currency.

## Formula

```
Detected Insider Dealing Breaches per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** corporate_governance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1047 (batch 4)
