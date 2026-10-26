# dea:metric-hospital-acquired-infection-rate

Candidate Performance Metric record for **Hospital-Acquired Infection Rate** (HAIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hospital-acquired-infection-rate`
- **Name:** Hospital-Acquired Infection Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HAIR

## 2. Definition

A Healthcare indicator, Hospital-Acquired Infection Rate (HAIR) quantifies exposure to adverse outcomes. It is defined as Healthcare-Associated Infections / Patient Days x 1,000; the result is stated in events per thousand or million (scaled). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. In Healthcare, it is a recognized element of the standard performance toolkit.

## 3. Context

Infections that were neither present nor incubating at admission, normalized per patient-day or per procedure - the metric category where quality becomes unambiguous, since these infections are by definition the hospital's own work. Its strategic weight is the surveillance-and-economics combination: public reporting regimes track specific categories (central-line infections, surgical-site, catheter-associated), and reimbursement systems increasingly deny payment for care required to treat them, converting infection prevention from best practice into revenue defense. The metric's diagnostic power is the device-linked structure: rates tied to specific devices respond to device-specific bundles (insertion checklists, maintenance protocols, removal prompts), which is why prevention programs manage by device line rather than by aggregate. Read the denominators carefully: procedure-linked rates need procedure counts, patient-day rates need honest patient-day capture, and rate movements sometimes reflect surveillance intensity rather than epidemiology - the persistent measurement trap of this family.

## Formula

```
HAIR = Healthcare-Associated Infections / Patient Days x 1,000
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** healthcare
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 465 (batch 1)
