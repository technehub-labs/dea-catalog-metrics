# dea:metric-safety-incident-frequency-construction

Candidate Performance Metric record for **Safety Incident Frequency (Construction)** (SIFC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-safety-incident-frequency-construction`
- **Name:** Safety Incident Frequency (Construction)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SIFC

## 2. Definition

A Construction & Engineering indicator, Safety Incident Frequency (Construction) (SIFC) quantifies exposure to adverse outcomes. It is defined as (Recordable Incidents x 200,000) / Total Hours Worked; the result is stated in ratio (x:1 or x). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. In Construction & engineering, it is a recognized element of the standard performance toolkit.

## 3. Context

Recordable safety incidents per hours worked - the construction industry's core safety metric, expressed in the same per-million-hours convention the sector inherited from heavy industry, and strategically the number that gates everything on a construction site: procurement frameworks increasingly require safety statistics in prequalification, so the metric is simultaneously an ethical indicator and a commercial asset. Its significance in construction specifically is the subcontracted-labor complexity: headcount is fluid, multi-employer sites blur accountability, and incident statistics that count only direct employees misrepresent the actual site risk - which is why mature regimes track contractor hours and incidents as one population. Read with the severity companion: frequency improving while severity worsens indicates the mix shifting toward fewer-but-graver events, the classic late-stage pattern of safety programs that have exhausted easy gains. The leading-indicator stack (near-miss reporting, inspection closure rates) is what moves this lagging number.

## Formula

```
SIFC = (Recordable Incidents x 200,000) / Total Hours Worked
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** construction_engineering
- **Sector:** construction_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 665 (batch 2)
