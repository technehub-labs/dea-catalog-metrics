# dea:metric-automation-oversight-burden

Canonical Performance Metric record for **Automation Oversight Burden (AOB)** in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-automation-oversight-burden`
- **Name:** Automation Oversight Burden
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate

## 2. Definition

Automation Oversight Burden (AOB) counts the human oversight events attributable to an automated path - escalations, scheduled reviews, and interventions - normalized per worker-day of the roles operating it, expressed as events per worker-day (ratio). It reads the staffing cost of supervision - where burden concentrates and whether the operating design keeps it sustainable. The record counts events; it does not judge the people handling them. Lower values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it supports operating-design, staffing, and workforce-impact decisions.

## 3. Purpose

Quantify the human supervision the automated path actually requires. Use to plan staffing for exception and review work, detect burden concentration, and inform workforce-impact and operating-design reviews.

## 4. Classification (CR-MET-002 binding 6 axes)

- **Subject classification:** operations
- **Purpose classification:** risk
- **Scope:** process
- **Directionality:** lower_is_better
- **Management significance:** operational, managerial

## 6. Unit or scale

- **Unit:** `dea:unit-ratio` (events per worker-day)

## 7. Formula (CR-MET-005 binding)

```
AOB = (Escalations + Scheduled Reviews + Interventions) / Worker-Days
```

Where the numerator counts oversight events attributable to the automated path in the window, and Worker-Days is the total worker-days of the operating roles in scope.

## 10. Frequency

Monthly.

## 12. Applicability (CR-MET-007 cross-domain)

- **Intended subjects:** `dea:BusinessProcess`, `dea:OrganizationalUnit`
- **Excluded subjects:** `dea:Outcome`

## 13. Relationships

- **External references:** broadens `mama-metrics:card/worker-experience-impact` (the card's oversight-burden component as a standalone record; see `external_references` in the record YAML)
- **Related records:** complements `dea:metric-human-in-the-loop-intervention-rate` (intervention share of interactions vs per-worker-day normalization)

## 14. Quality

- **Validation:** Events MUST be attributable to the automated path; the denominator population MUST be stated with the value.
- **Known limitations:** Event counts do not weigh effort; suppressed or off-system handling undercounts the burden.

## 19. References

- MAMA (Measuring Automation & Measuring Autonomy) mama-metrics metric library v0.1.1 (CC-BY-4.0), card `worker-experience-impact` (oversight-burden component)
- OpenDEAM dea-metamodel CR-MET-001 / CR-MET-005 / CR-MET-007 bindings
