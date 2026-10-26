# dea:metric-theft-and-shrink-incident-value

Candidate Performance Metric record for **Theft and Shrink Incident Value** (TSIV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-theft-and-shrink-incident-value`
- **Name:** Theft and Shrink Incident Value
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TSIV

## 2. Definition

Theft and Shrink Incident Value (TSIV) measures exposure to adverse outcomes in the Physical Security Operations domain. It is defined as Value of Confirmed Theft and Loss Events per Period; the result is stated in currency value. It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Theft and shrink incident value measures the monetary loss from theft, fraud, and inventory shrinkage, and it is the direct-loss metric of physical security and asset protection - the number that prices the security program against its cost. Shrink decomposition is the management information: external theft, internal theft, administrative and paperwork error, and vendor fraud each need different countermeasures, and the retail industry's shrink surveys consistently show the internal-and-process share is larger than the shoplifting share. The measurement is audit-based (inventory counts versus book), so count-accuracy and cadence determine the number's reliability, and detected-versus-undetected loss requires estimation (self-reported shrink understates). Read with loss per incident trend, category-level shrink concentration, investigation-case value recovery, and control-metric performance (EAS tag compliance, POS exception monitoring hits).

## Formula

```
TSIV = Value of Confirmed Theft and Loss Events per Period
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** physical_security_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1211 (batch 4)
