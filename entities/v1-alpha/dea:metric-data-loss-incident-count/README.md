# dea:metric-data-loss-incident-count

Candidate Performance Metric record for **Data Loss Incident Count** (DLIC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-loss-incident-count`
- **Name:** Data Loss Incident Count
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DLIC

## 2. Definition

Data Loss Incident Count (DLIC) measures exposure to adverse outcomes in the Cybersecurity domain. It is defined as Confirmed Data Loss or Leakage Events; the result is stated in count (items per period). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The number of events in which data was lost, leaked, or exposed - whether by breach, misdelivery, misconfiguration, or disposal failure. Its strategic weight is regulatory: data protection regimes from GDPR onward attach notification duties and potentially percentage-of-revenue penalties to personal-data incidents, which converts this count from a technical tally into a legal and reputational exposure ledger. The honest analysis is by cause, because the remedies differ completely - external intrusion demands security investment, misdelivery and misconfiguration demand process and access design, and insider events demand a different response entirely. The known reporting distortion is that this count rises with detection maturity, exactly like incident counts, so trends must be read against the detection-capability baseline before concluding the situation is worsening.

## Formula

```
Confirmed Data Loss or Leakage Events
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cybersecurity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 333 (batch 1)
