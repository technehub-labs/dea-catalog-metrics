# dea:metric-repeat-defect-rate-aviation

Candidate Performance Metric record for **Repeat Defect Rate (Aviation)** (RDR-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-repeat-defect-rate-aviation`
- **Name:** Repeat Defect Rate (Aviation)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RDR-A

## 2. Definition

Repeat Defect Rate (Aviation) (RDR-A) measures the quality of outputs and outcomes in the Aviation Maintenance Repair & Overhaul domain. It is computed as Defects Recurring after Repair / Repairs Performed, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is concentrated in Airlines & aviation.

## 3. Context

Measures aircraft defects recurring after certified repair. It matters because repeat defects in aviation are airworthiness and safety signals, not just cost. Reclassification of recurring defects as new fault codes hides the pattern. Read with Component Repair Turnaround Time and Maintenance Quality Audit findings to confirm repairs hold.

## Formula

```
RDR-A = Defects Recurring after Repair / Repairs Performed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** aviation_maintenance_repair_overhaul
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1186 (batch 4)
