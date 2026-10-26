# dea:metric-time-to-regulatory-decision

Candidate Performance Metric record for **Time to Regulatory Decision** (TTRD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-regulatory-decision`
- **Name:** Time to Regulatory Decision
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TTRD

## 2. Definition

Time to Regulatory Decision (TTRD) addresses how efficiently resources are converted into outputs and is a fixture of pharma r&d & clinical trials reporting. It is computed as Days from Submission to Regulatory Decision, expressed in days. Its use is concentrated in Pharmaceuticals. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures elapsed time from submission to agency decision. It anchors launch economics and exclusivity runway, since months of delay are pure lost value for in-patent assets. Controllable drivers (quality of the submission, responses to information requests) differ from external ones (agency workload, review pathways), so separate them before benchmarking. Read with regulatory submission acceptance rate and post-marketing commitments assumed at approval.

## Formula

```
Days from Submission to Regulatory Decision
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1622 (batch 6)
