# dea:metric-student-to-faculty-ratio

Candidate Performance Metric record for **Student-to-Faculty Ratio** (SFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-student-to-faculty-ratio`
- **Name:** Student-to-Faculty Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SFR

## 2. Definition

Student-to-Faculty Ratio (SFR) measures the utilization or availability of capacity in the Education domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Enrolled Students / Faculty Members - reported in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. It is a standard measure in the Education sector.

## 3. Context

Enrolled students per instructional faculty member - the structural metric of the academic operating model, sitting between quality and economics: lower ratios are the conventional proxy for contact quality, higher ratios are the operating-leverage reality of mass higher education, and every institution's mission statement sits somewhere on that trade. Its strategic significance is the cost structure it encodes - faculty compensation is the dominant cost line in the education model, so the ratio is the primary driver of cost per student and margin - which is why the metric moves glacially and why adjunct-heavy models that lower the apparent ratio while degrading the real one are the sector's standard coping mechanism. The honest comparison needs the definitions reconciled: what counts as faculty (full-time, adjunct, instructional versus research) varies enough between institutions that raw ratios mislead.

## Formula

```
SFR = Enrolled Students / Faculty Members
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** capability
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** education
- **Sector:** education

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 516 (batch 1)
