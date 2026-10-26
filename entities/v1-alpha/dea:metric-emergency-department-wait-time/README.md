# dea:metric-emergency-department-wait-time

Candidate Performance Metric record for **Emergency Department Wait Time** (EDWT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-emergency-department-wait-time`
- **Name:** Emergency Department Wait Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EDWT

## 2. Definition

Emergency Department Wait Time (EDWT) captures how efficiently resources are converted into outputs for organizations tracking healthcare. Its calculation is Median Minutes from Arrival to Treatment, measured in minutes. It originates from and is most used in Healthcare practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Elapsed time from emergency arrival to care - conventionally the time to see a clinician, sometimes the door-to-disposition interval - the metric that sits at the intersection of clinical risk and patient experience, since emergency waits are the waits where delay is measured in outcomes rather than dissatisfaction. Its strategic significance is the queueing reality it exposes: ED wait times are mostly not emergency-department problems but boarding problems - admitted patients holding ED beds while inpatient beds are unavailable upstream - which is why the honest fix is hospital-wide capacity and discharge timing, not ED staffing alone. Read with the acuity split: waits for low-acuity arrivals are a satisfaction issue, waits for high-acuity arrivals are a safety issue, and headline averages blur them - which is why severity-stratified waits plus left-without-being-seen rate form the honest picture of ED performance.

## Formula

```
EDWT = Median Minutes from Arrival to Treatment
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 463 (batch 1)
