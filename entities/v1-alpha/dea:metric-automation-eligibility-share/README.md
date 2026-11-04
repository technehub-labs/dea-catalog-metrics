# dea:metric-automation-eligibility-share

Canonical Performance Metric record for **Automation Eligibility Share (AES)** in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-automation-eligibility-share`
- **Name:** Automation Eligibility Share
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate

## 2. Definition

Automation Eligibility Share (AES) quantifies the automatable base of a process - the share of assessed work items classified eligible for automation under documented, versioned criteria. The formula is Work Items Classified Eligible / Assessed Work Items - reported in percent (%). Eligibility judgments are assessor-dependent, so the criteria version and inter-assessor agreement are part of any reported value. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it supports automation scoping, eligibility assessment, and investment decisions.

## 3. Purpose

Quantify how much of an assessed process is automatable before automation investment is committed. Use to scope automation programs, compare candidate processes for investment, and provide the denominator basis for automation coverage measures.

## 4. Classification (CR-MET-002 binding 6 axes)

- **Subject classification:** business_architecture
- **Purpose classification:** capability
- **Scope:** process
- **Directionality:** higher_is_better
- **Management significance:** operational, managerial

## 6. Unit or scale

- **Unit:** `dea:unit-ratio-percent` (CR-MET-017 canonical ratio-percent form)

## 7. Formula (CR-MET-005 binding)

```
AES = (Work Items Classified Eligible / Assessed Work Items) * 100
```

Where the numerator counts assessed work items classified eligible under the documented criteria version, and the denominator counts all assessed work items in scope for the window.

## 10. Frequency

Quarterly, or on process or criteria change.

## 12. Applicability (CR-MET-007 cross-domain)

- **Intended subjects:** `dea:BusinessProcess`, `dea:ValueStream`
- **Excluded subjects:** `dea:Outcome`

## 13. Relationships

- **External references:** aligns_with `mama-metrics:card/automation-eligibility-share` (source definition; see `external_references` in the record YAML)
- **Related records:** complements `dea:metric-automation-potential-realized-rate` and `dea:metric-automation-ratio` (coverage constructs that presuppose an eligibility basis)

## 14. Quality

- **Validation:** Eligibility criteria version MUST be recorded with every reported value; items without a completed assessment MUST be excluded and reported separately as assessment coverage.
- **Known limitations:** High eligibility is not high value or benefit; permissive criteria inflate the share, so criteria versions are part of the provenance.

## 19. References

- MAMA (Measuring Automation & Measuring Autonomy) mama-metrics metric library v0.1.1 (CC-BY-4.0), card `automation-eligibility-share`
- OpenDEAM dea-metamodel CR-MET-001 / CR-MET-005 / CR-MET-007 bindings
