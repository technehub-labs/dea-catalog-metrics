# dea:metric-straight-through-processing-rate-underwriting

Candidate Performance Metric record for **Straight-Through Processing Rate (Underwriting)** (STPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-straight-through-processing-rate-underwriting`
- **Name:** Straight-Through Processing Rate (Underwriting)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** STPU

## 2. Definition

Straight-Through Processing Rate (Underwriting) (STPU) captures how efficiently resources are converted into outputs for organizations tracking insurance underwriting. It is computed as Policies Issued without Manual Touch / Policies Issued, expressed in percent (%). Its use is concentrated in Insurance. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of applications underwritten end-to-end by rules and models without human intervention. It is the efficiency and customer-speed frontier of underwriting transformation, and a risk-quality lever when automation is well governed. The dual gaming risks: clean-upstream risk (humans pre-screen applications so the bot only sees easy cases) and silent decline loops where automated referrals quietly reject. Read with automated decision approval rate and loss ratio by STP versus manual cohort.

## Formula

```
Policies Issued without Manual Touch / Policies Issued
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1503 (batch 6)
