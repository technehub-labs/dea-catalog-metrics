# dea:metric-pipeline-attrition-rate

Candidate Performance Metric record for **Pipeline Attrition Rate** (PAR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pipeline-attrition-rate`
- **Name:** Pipeline Attrition Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PAR-P

## 2. Definition

Within Pharma R&D & Clinical Trials, Pipeline Attrition Rate (PAR-P) is used to gauge exposure to adverse outcomes. It is computed as Candidates Discontinued / Candidates in Development, expressed in percent (%). Its use is concentrated in Pharmaceuticals. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of pipeline candidates terminated per period, by phase and reason. Attrition is not failure but the operating cost of the discovery model; what matters is whether termination reasons match the portfolio thesis and happen early enough to redeploy capital. Watch for zombie programs kept alive for strategic sentiment, and for late-phase terminations that early data already predicted. Read with phase transition success rate and R&D pipeline value.

## Formula

```
Candidates Discontinued / Candidates in Development
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** pharma_r_d_clinical_trials
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1623 (batch 6)
